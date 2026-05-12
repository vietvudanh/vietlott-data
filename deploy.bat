@echo off

echo Starting Docker daemon...
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"

echo Waiting for Docker to be ready...
:waitloop
docker info >nul 2>&1
if errorlevel 1 (
    timeout /t 3 /nobreak >nul
    goto waitloop
)
echo Docker is ready.

echo Building Docker image...
docker build -t vietlott-prediction .
if errorlevel 1 (
    echo Docker build failed.
    pause
    exit /b 1
)

echo Tagging Docker image...
docker tag vietlott-prediction:latest 292118947232.dkr.ecr.ap-southeast-2.amazonaws.com/vietlott-prediction:latest

echo Logging in to AWS (browser will open)...
aws login
if errorlevel 1 (
    echo AWS login failed.
    pause
    exit /b 1
)

echo Authenticating Docker with ECR...
aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 292118947232.dkr.ecr.ap-southeast-2.amazonaws.com
if errorlevel 1 (
    echo ECR login failed.
    pause
    exit /b 1
)

echo Pushing Docker image...
docker push 292118947232.dkr.ecr.ap-southeast-2.amazonaws.com/vietlott-prediction:latest
if errorlevel 1 (
    echo Docker push failed.
    pause
    exit /b 1
)

echo All done. Image pushed successfully.
pause
