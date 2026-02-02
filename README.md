# GPT Computer Use Demo

A Python demonstration of using Azure OpenAI's GPT Computer Use model to automate web browser interactions. This demo navigates to the Microsoft Fabric API documentation, clicks on navigation items, and summarizes the content.

## Overview

This demo showcases the GPT Computer Use model's ability to:
- Navigate to web pages
- Interact with page elements (clicking navigation items)
- Analyze page content using screenshots
- Provide summaries of documentation

## Prerequisites

1. **Azure OpenAI Access**: You need access to Azure OpenAI's Computer Use model (preview). This is a limited access feature that requires approval from Microsoft.

2. **Python 3.8+**: Make sure you have Python 3.8 or higher installed.

3. **Azure OpenAI Deployment**: You should have a Computer Use model deployed in Azure OpenAI Service in a supported region (East US 2, Sweden Central, or South India).

## Installation

1. Clone this repository:
```bash
git clone https://github.com/7effrey89/gpt-computer-use-demo.git
cd gpt-computer-use-demo
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Install Playwright browsers:
```bash
playwright install chromium
```

## Configuration

1. Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

2. Edit the `.env` file and add your Azure OpenAI credentials:
```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=computer-use-preview
```

Alternatively, you can set these as environment variables:
```bash
export AZURE_OPENAI_ENDPOINT='https://your-resource.openai.azure.com/'
export AZURE_OPENAI_API_KEY='your-api-key'
export AZURE_OPENAI_DEPLOYMENT_NAME='computer-use-preview'
```

## Usage

Run the demo:
```bash
python demo.py
```

The demo will:
1. Launch a browser
2. Navigate to https://learn.microsoft.com/en-us/rest/api/fabric/articles/api-structure
3. Click on "Identity Scope" in the left navigation
4. Use the Computer Use model to summarize the page content
5. Click on "Throttling" in the left navigation
6. Use the Computer Use model to summarize that page content
7. Output both summaries to the console

## How It Works

The Computer Use model works through a loop:
1. **Capture**: Take a screenshot of the current browser state
2. **Analyze**: Send the screenshot and instructions to the Computer Use model
3. **Act**: The model returns action plans (in this case, summaries)
4. **Repeat**: Continue the loop for the next task

This demo simplifies the process by using Playwright for browser automation and focusing on the content summarization aspect of the Computer Use model.

## Demo Workflow

```
┌─────────────────────────────────────────────┐
│  Start Browser & Navigate to Target Page   │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Click "Identity Scope" Navigation Item     │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Take Screenshot → Send to GPT Model        │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Receive & Display Summary in Console       │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Click "Throttling" Navigation Item         │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Take Screenshot → Send to GPT Model        │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Receive & Display Summary in Console       │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Close Browser & Complete                   │
└─────────────────────────────────────────────┘
```

## Security Considerations

⚠️ **Important**: The Computer Use model has significant security implications:

- Run only in sandboxed or isolated environments
- Be cautious of prompt injection risks
- Review and validate all actions before execution in production
- Avoid using on sensitive systems or with sensitive data
- Always require user consent for destructive operations

## Troubleshooting

### "AZURE_OPENAI_ENDPOINT environment variable is not set"
Make sure you've set the required environment variables or created a `.env` file with your credentials.

### "Error calling Computer Use model"
- Verify your Azure OpenAI endpoint and API key are correct
- Ensure your deployment has access to the Computer Use model
- Check that your deployment name matches the one in your configuration

### Browser doesn't launch
Run `playwright install chromium` to ensure Playwright browsers are installed.

## References

- [Azure OpenAI Computer Use Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/computer-use)
- [Azure-Samples/computer-use-model](https://github.com/Azure-Samples/computer-use-model)
- [Microsoft Fabric API Documentation](https://learn.microsoft.com/en-us/rest/api/fabric/articles/api-structure)

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.