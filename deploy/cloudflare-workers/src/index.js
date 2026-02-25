/**
 * Cloudflare Worker to trigger Vietlott data crawling
 * 
 * Since Cloudflare Workers has limited Python support and cannot run
 * heavy libraries like polars/pandas, this worker serves as a scheduler
 * that triggers the actual crawling process via:
 * 
 * 1. GitHub Actions workflow dispatch (recommended)
 * 2. AWS Lambda function invocation
 * 3. External API endpoint
 * 
 * @author Viet Vu
 */

// Configuration - Set these in wrangler.toml or environment
const CONFIG = {
    // GitHub configuration for workflow dispatch
    GITHUB_REPO: 'vietvudanh/vietlott-data',
    GITHUB_WORKFLOW: 'crawl.yaml',
    
    // AWS Lambda configuration (alternative)
    AWS_LAMBDA_URL: null, // Set if using Lambda function URL
    
    // Custom backend URL (alternative)
    BACKEND_URL: null,
};

/**
 * Trigger GitHub Actions workflow via workflow_dispatch
 * @param {string} token - GitHub personal access token
 * @param {string} repo - Repository in format 'owner/repo'
 * @param {string} workflow - Workflow file name
 * @returns {Promise<Response>}
 */
async function triggerGitHubWorkflow(token, repo, workflow) {
    const url = `https://api.github.com/repos/${repo}/actions/workflows/${workflow}/dispatches`;
    
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/vnd.github.v3+json',
            'Authorization': `Bearer ${token}`,
            'User-Agent': 'Vietlott-Cloudflare-Worker',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            ref: 'main',
            inputs: {
                triggered_by: 'cloudflare-worker',
                timestamp: new Date().toISOString(),
            }
        }),
    });
    
    if (response.status === 204) {
        return new Response(JSON.stringify({
            success: true,
            message: 'GitHub workflow triggered successfully',
            workflow: workflow,
            repo: repo,
            timestamp: new Date().toISOString(),
        }), {
            headers: { 'Content-Type': 'application/json' },
        });
    }
    
    const error = await response.text();
    return new Response(JSON.stringify({
        success: false,
        message: 'Failed to trigger GitHub workflow',
        error: error,
        status: response.status,
    }), {
        status: response.status,
        headers: { 'Content-Type': 'application/json' },
    });
}

/**
 * Trigger AWS Lambda function via function URL
 * @param {string} lambdaUrl - Lambda function URL
 * @returns {Promise<Response>}
 */
async function triggerLambda(lambdaUrl) {
    const response = await fetch(lambdaUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            source: 'cloudflare-worker',
            timestamp: new Date().toISOString(),
        }),
    });
    
    const result = await response.json();
    return new Response(JSON.stringify({
        success: response.ok,
        message: response.ok ? 'Lambda function triggered' : 'Lambda trigger failed',
        result: result,
    }), {
        status: response.status,
        headers: { 'Content-Type': 'application/json' },
    });
}

/**
 * Main request handler
 */
export default {
    /**
     * Handle HTTP requests
     * @param {Request} request
     * @param {object} env - Environment bindings
     * @param {object} ctx - Execution context
     * @returns {Promise<Response>}
     */
    async fetch(request, env, ctx) {
        const url = new URL(request.url);
        
        // Health check endpoint
        if (url.pathname === '/health') {
            return new Response(JSON.stringify({
                status: 'healthy',
                service: 'vietlott-crawler-trigger',
                timestamp: new Date().toISOString(),
            }), {
                headers: { 'Content-Type': 'application/json' },
            });
        }
        
        // Status endpoint
        if (url.pathname === '/status') {
            return new Response(JSON.stringify({
                service: 'vietlott-crawler-trigger',
                mode: env.GITHUB_TOKEN ? 'github-workflow' : 
                      env.AWS_LAMBDA_URL ? 'aws-lambda' : 
                      env.BACKEND_URL ? 'custom-backend' : 'not-configured',
                github_repo: CONFIG.GITHUB_REPO,
                github_workflow: CONFIG.GITHUB_WORKFLOW,
            }), {
                headers: { 'Content-Type': 'application/json' },
            });
        }
        
        // Trigger endpoint
        if (url.pathname === '/trigger' || url.pathname === '/') {
            // Only allow POST for trigger, or GET with secret
            if (request.method !== 'POST') {
                const secret = url.searchParams.get('secret');
                if (!secret || secret !== env.TRIGGER_SECRET) {
                    return new Response(JSON.stringify({
                        error: 'Method not allowed or missing secret',
                        message: 'Use POST request or provide secret query parameter',
                    }), {
                        status: 405,
                        headers: { 'Content-Type': 'application/json' },
                    });
                }
            }
            
            // Priority: GitHub > Lambda > Custom Backend
            if (env.GITHUB_TOKEN) {
                return await triggerGitHubWorkflow(
                    env.GITHUB_TOKEN,
                    env.GITHUB_REPO || CONFIG.GITHUB_REPO,
                    env.GITHUB_WORKFLOW || CONFIG.GITHUB_WORKFLOW
                );
            }
            
            if (env.AWS_LAMBDA_URL) {
                return await triggerLambda(env.AWS_LAMBDA_URL);
            }
            
            if (env.BACKEND_URL) {
                return await triggerLambda(env.BACKEND_URL);
            }
            
            return new Response(JSON.stringify({
                error: 'Not configured',
                message: 'Please set GITHUB_TOKEN, AWS_LAMBDA_URL, or BACKEND_URL environment variable',
            }), {
                status: 500,
                headers: { 'Content-Type': 'application/json' },
            });
        }
        
        // 404 for unknown paths
        return new Response(JSON.stringify({
            error: 'Not found',
            available_endpoints: ['/health', '/status', '/trigger'],
        }), {
            status: 404,
            headers: { 'Content-Type': 'application/json' },
        });
    },
    
    /**
     * Handle scheduled events (Cron Triggers)
     * @param {ScheduledEvent} event
     * @param {object} env
     * @param {object} ctx
     */
    async scheduled(event, env, ctx) {
        console.log('Scheduled trigger fired:', event.cron);
        
        if (env.GITHUB_TOKEN) {
            const response = await triggerGitHubWorkflow(
                env.GITHUB_TOKEN,
                env.GITHUB_REPO || CONFIG.GITHUB_REPO,
                env.GITHUB_WORKFLOW || CONFIG.GITHUB_WORKFLOW
            );
            console.log('GitHub workflow trigger result:', await response.text());
        } else if (env.AWS_LAMBDA_URL) {
            const response = await triggerLambda(env.AWS_LAMBDA_URL);
            console.log('Lambda trigger result:', await response.text());
        } else {
            console.error('No trigger configured');
        }
    },
};
