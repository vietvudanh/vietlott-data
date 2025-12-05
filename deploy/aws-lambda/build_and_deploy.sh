#!/bin/bash
#
# Build and deploy script for AWS Lambda
# This script creates a deployment package with all dependencies
#
# Prerequisites:
# - AWS CLI configured with appropriate credentials
# - Python 3.11+ installed
# - pip and zip installed
#
# Usage:
#   ./build_and_deploy.sh [--function-name <name>] [--region <region>]
#
# Environment Variables (can be set in .env file):
#   AWS_LAMBDA_FUNCTION_NAME - Name of the Lambda function
#   AWS_REGION - AWS region for deployment
#   GITHUB_TOKEN - GitHub token (set as Lambda env var, not here)
#   GITHUB_REPO - Repository in format 'owner/repo'

set -e

# Default values
FUNCTION_NAME="${AWS_LAMBDA_FUNCTION_NAME:-vietlott-data-crawler}"
REGION="${AWS_REGION:-us-east-1}"
RUNTIME="python3.11"
HANDLER="lambda_function.lambda_handler"
TIMEOUT=900  # 15 minutes
MEMORY_SIZE=1024  # 1GB

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --function-name)
            FUNCTION_NAME="$2"
            shift 2
            ;;
        --region)
            REGION="$2"
            shift 2
            ;;
        --create)
            CREATE_FUNCTION=true
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Directories
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
BUILD_DIR="$SCRIPT_DIR/build"
LAYER_DIR="$SCRIPT_DIR/layer"

echo "=== Vietlott Data Lambda Deployment ==="
echo "Function Name: $FUNCTION_NAME"
echo "Region: $REGION"
echo "Project Root: $PROJECT_ROOT"

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf "$BUILD_DIR" "$LAYER_DIR"
mkdir -p "$BUILD_DIR" "$LAYER_DIR/python"

# Install dependencies for Lambda layer
echo "Installing dependencies..."
pip install \
    --platform manylinux2014_x86_64 \
    --target "$LAYER_DIR/python" \
    --implementation cp \
    --python-version 3.11 \
    --only-binary=:all: \
    --upgrade \
    -r "$PROJECT_ROOT/requirements.txt"

# Copy source code to build directory
echo "Copying source code..."
cp "$SCRIPT_DIR/lambda_function.py" "$BUILD_DIR/"
cp -r "$PROJECT_ROOT/src" "$BUILD_DIR/"

# Create deployment package
echo "Creating deployment package..."
cd "$BUILD_DIR"
zip -r9 "../lambda_function.zip" .

# Create layer package
echo "Creating layer package..."
cd "$LAYER_DIR"
zip -r9 "../lambda_layer.zip" .

cd "$SCRIPT_DIR"

# Check if function exists
FUNCTION_EXISTS=$(aws lambda get-function --function-name "$FUNCTION_NAME" --region "$REGION" 2>&1 || true)

if [[ "$FUNCTION_EXISTS" == *"ResourceNotFoundException"* ]] || [[ "$CREATE_FUNCTION" == "true" ]]; then
    echo "Creating new Lambda function..."
    
    # First, create or get the layer
    LAYER_ARN=$(aws lambda publish-layer-version \
        --layer-name "${FUNCTION_NAME}-deps" \
        --description "Dependencies for Vietlott data crawler" \
        --zip-file "fileb://lambda_layer.zip" \
        --compatible-runtimes "$RUNTIME" \
        --region "$REGION" \
        --query 'LayerVersionArn' \
        --output text)
    
    echo "Created layer: $LAYER_ARN"
    
    # Create the function
    aws lambda create-function \
        --function-name "$FUNCTION_NAME" \
        --runtime "$RUNTIME" \
        --handler "$HANDLER" \
        --role "arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):role/lambda-execution-role" \
        --zip-file "fileb://lambda_function.zip" \
        --timeout "$TIMEOUT" \
        --memory-size "$MEMORY_SIZE" \
        --layers "$LAYER_ARN" \
        --region "$REGION" \
        --environment "Variables={LOGURU_LEVEL=INFO,PYTHONPATH=/opt/python:/var/task/src}"
    
    echo "Function created successfully!"
else
    echo "Updating existing Lambda function..."
    
    # Update the layer
    LAYER_ARN=$(aws lambda publish-layer-version \
        --layer-name "${FUNCTION_NAME}-deps" \
        --description "Dependencies for Vietlott data crawler" \
        --zip-file "fileb://lambda_layer.zip" \
        --compatible-runtimes "$RUNTIME" \
        --region "$REGION" \
        --query 'LayerVersionArn' \
        --output text)
    
    echo "Updated layer: $LAYER_ARN"
    
    # Update function code
    aws lambda update-function-code \
        --function-name "$FUNCTION_NAME" \
        --zip-file "fileb://lambda_function.zip" \
        --region "$REGION"
    
    # Wait for function to be updated
    echo "Waiting for function update to complete..."
    aws lambda wait function-updated --function-name "$FUNCTION_NAME" --region "$REGION"
    
    # Update function configuration
    aws lambda update-function-configuration \
        --function-name "$FUNCTION_NAME" \
        --timeout "$TIMEOUT" \
        --memory-size "$MEMORY_SIZE" \
        --layers "$LAYER_ARN" \
        --region "$REGION"
    
    echo "Function updated successfully!"
fi

# Clean up build artifacts
echo "Cleaning up..."
rm -rf "$BUILD_DIR" "$LAYER_DIR"

echo ""
echo "=== Deployment Complete ==="
echo "Function ARN: $(aws lambda get-function --function-name "$FUNCTION_NAME" --region "$REGION" --query 'Configuration.FunctionArn' --output text)"
echo ""
echo "Don't forget to set environment variables:"
echo "  aws lambda update-function-configuration \\"
echo "    --function-name $FUNCTION_NAME \\"
echo "    --environment 'Variables={GITHUB_TOKEN=your_token,GITHUB_REPO=vietvudanh/vietlott-data,GIT_USER_NAME=Lambda Bot,GIT_USER_EMAIL=bot@example.com}'"
