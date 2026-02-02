# Example Output

This file shows an example of what the demo output looks like when running with valid Azure OpenAI credentials.

```
============================================================
GPT Computer Use Demo
============================================================

This demo will:
1. Navigate to the Microsoft Fabric API Structure documentation
2. Click on 'Identity Scope' and summarize the content
3. Click on 'Throttling' and summarize the content

Required environment variables:
  - AZURE_OPENAI_ENDPOINT: Your Azure OpenAI endpoint
  - AZURE_OPENAI_API_KEY: Your API key (or use Azure credential)
  - AZURE_OPENAI_DEPLOYMENT_NAME: Your deployment name (default: computer-use-preview)
============================================================

Starting browser...

=== Navigating to https://learn.microsoft.com/en-us/rest/api/fabric/articles/api-structure ===

============================================================
TASK 1: Identity Scope
============================================================

=== Clicking on 'Identity Scope' in navigation ===

--- Summary of 'Identity Scope' page ---
The Identity Scope documentation explains how authentication and authorization work in Microsoft Fabric's REST API. Key points include:

1. **Authentication Methods**: The API supports Azure Active Directory (Azure AD) authentication using OAuth 2.0 tokens. Applications must register with Azure AD to obtain credentials.

2. **Token Acquisition**: Applications need to acquire access tokens using the Azure AD authentication flow. The token should be included in the Authorization header of API requests as a Bearer token.

3. **Scopes and Permissions**: Different API operations require different permission scopes. Applications must request the appropriate scopes when obtaining tokens. Common scopes include:
   - https://analysis.windows.net/powerbi/api/.default for Power BI APIs
   - User_Impersonation for delegated permissions

4. **Security Best Practices**: 
   - Store credentials securely
   - Use the principle of least privilege
   - Refresh tokens before expiration
   - Implement proper error handling for authentication failures

5. **Service Principal vs User Authentication**: The documentation covers both service principal (application) authentication and user-delegated authentication scenarios.
------------------------------------------------------------

============================================================
TASK 2: Throttling
============================================================

=== Clicking on 'Throttling' in navigation ===

--- Summary of 'Throttling' page ---
The Throttling documentation describes rate limiting and request throttling mechanisms in Microsoft Fabric's REST API. Main concepts include:

1. **Rate Limits**: Microsoft Fabric implements rate limits to ensure service stability and fair usage. Different API operations may have different rate limits based on:
   - Number of requests per time window
   - Resource consumption
   - Tenant and capacity limits

2. **HTTP Status Codes**: When rate limits are exceeded, the API returns:
   - HTTP 429 (Too Many Requests) status code
   - Retry-After header indicating when to retry the request

3. **Throttling Strategies**:
   - Implement exponential backoff when encountering 429 responses
   - Respect the Retry-After header value
   - Distribute API calls over time rather than bursting
   - Use batch operations where available

4. **Capacity Management**: Rate limits are influenced by:
   - Fabric capacity assignment
   - Concurrent operations per capacity
   - Resource-intensive operations may have stricter limits

5. **Best Practices**:
   - Monitor response headers for rate limit information
   - Implement retry logic with exponential backoff
   - Cache responses when possible to reduce API calls
   - Use webhooks or change notifications instead of polling
   - Consider load balancing across multiple time periods

6. **Error Handling**: Proper error handling should include:
   - Detecting 429 status codes
   - Reading Retry-After headers
   - Implementing graceful degradation
   - Logging throttling events for monitoring
------------------------------------------------------------

============================================================
Demo completed successfully!
============================================================

Closing browser...
```

## Notes

- The actual summaries will vary based on the current content of the Microsoft Learn pages
- The Computer Use model analyzes screenshots of the pages to generate these summaries
- Response times depend on the model's performance and network conditions
- The demo uses Playwright in non-headless mode so you can see the browser automation in action
