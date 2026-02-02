"""
GPT Computer Use Demo
This demo uses the Azure OpenAI Computer Use model to navigate a webpage,
interact with navigation elements, and summarize content.
"""

import os
import base64
import json
from io import BytesIO
from playwright.sync_api import sync_playwright
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


class ComputerUseDemo:
    def __init__(self):
        """Initialize the demo with Azure OpenAI client and browser."""
        # Azure OpenAI configuration
        # These should be set as environment variables
        self.endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "computer-use-preview")
        
        # Initialize Azure OpenAI client
        if self.api_key:
            self.client = AzureOpenAI(
                api_version="2024-12-01-preview",
                azure_endpoint=self.endpoint,
                api_key=self.api_key
            )
        else:
            # Use DefaultAzureCredential for authentication
            token_provider = get_bearer_token_provider(
                DefaultAzureCredential(),
                "https://cognitiveservices.azure.com/.default"
            )
            self.client = AzureOpenAI(
                api_version="2024-12-01-preview",
                azure_endpoint=self.endpoint,
                azure_ad_token_provider=token_provider
            )
        
        self.browser = None
        self.page = None
        
    def start_browser(self):
        """Start the Playwright browser."""
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(viewport={'width': 1280, 'height': 720})
        self.page = self.context.new_page()
        
    def stop_browser(self):
        """Stop the browser and cleanup."""
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()
            
    def take_screenshot(self):
        """Take a screenshot and return as base64 encoded string."""
        screenshot_bytes = self.page.screenshot()
        return base64.b64encode(screenshot_bytes).decode('utf-8')
    
    def get_computer_use_action(self, instruction, screenshot_b64):
        """
        Send instruction and screenshot to the Computer Use model
        and get the next action to perform.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.deployment_name,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": instruction
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{screenshot_b64}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=4096
            )
            
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error calling Computer Use model: {e}")
            return None
    
    def summarize_content(self, screenshot_b64):
        """Ask the model to summarize the current page content."""
        instruction = (
            "Please analyze this webpage screenshot and provide a concise summary "
            "of the main content and key points. Focus on the technical documentation "
            "and important information presented."
        )
        
        summary = self.get_computer_use_action(instruction, screenshot_b64)
        return summary
    
    def navigate_to_page(self, url):
        """Navigate to the specified URL."""
        print(f"\n=== Navigating to {url} ===")
        self.page.goto(url, wait_until="networkidle")
        self.page.wait_for_timeout(2000)  # Wait for page to fully load
        
    def click_navigation_item(self, item_text):
        """Click on a navigation item by its text."""
        print(f"\n=== Clicking on '{item_text}' in navigation ===")
        try:
            # Try to find and click the navigation item
            # Look for the item in the left navigation
            element = self.page.locator(f"text={item_text}").first
            element.click()
            self.page.wait_for_timeout(2000)  # Wait for content to load
            return True
        except Exception as e:
            print(f"Error clicking navigation item: {e}")
            return False
    
    def run_demo(self):
        """Run the main demo workflow."""
        try:
            # Start browser
            print("Starting browser...")
            self.start_browser()
            
            # Navigate to the target page
            target_url = "https://learn.microsoft.com/en-us/rest/api/fabric/articles/api-structure"
            self.navigate_to_page(target_url)
            
            # Task 1: Click on "Identity Scope" and summarize
            print("\n" + "="*60)
            print("TASK 1: Identity Scope")
            print("="*60)
            
            if self.click_navigation_item("Identity Scope"):
                screenshot = self.take_screenshot()
                summary = self.summarize_content(screenshot)
                
                print("\n--- Summary of 'Identity Scope' page ---")
                print(summary)
                print("-" * 60)
            else:
                print("Failed to click on 'Identity Scope'")
            
            # Task 2: Click on "Throttling" and summarize
            print("\n" + "="*60)
            print("TASK 2: Throttling")
            print("="*60)
            
            if self.click_navigation_item("Throttling"):
                screenshot = self.take_screenshot()
                summary = self.summarize_content(screenshot)
                
                print("\n--- Summary of 'Throttling' page ---")
                print(summary)
                print("-" * 60)
            else:
                print("Failed to click on 'Throttling'")
            
            print("\n" + "="*60)
            print("Demo completed successfully!")
            print("="*60)
            
        except Exception as e:
            print(f"Error during demo: {e}")
            import traceback
            traceback.print_exc()
        finally:
            # Cleanup
            print("\nClosing browser...")
            self.stop_browser()


def main():
    """Main entry point for the demo."""
    print("="*60)
    print("GPT Computer Use Demo")
    print("="*60)
    print("\nThis demo will:")
    print("1. Navigate to the Microsoft Fabric API Structure documentation")
    print("2. Click on 'Identity Scope' and summarize the content")
    print("3. Click on 'Throttling' and summarize the content")
    print("\nRequired environment variables:")
    print("  - AZURE_OPENAI_ENDPOINT: Your Azure OpenAI endpoint")
    print("  - AZURE_OPENAI_API_KEY: Your API key (or use Azure credential)")
    print("  - AZURE_OPENAI_DEPLOYMENT_NAME: Your deployment name (default: computer-use-preview)")
    print("="*60 + "\n")
    
    # Check for required environment variables
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    if not endpoint:
        print("ERROR: AZURE_OPENAI_ENDPOINT environment variable is not set!")
        print("\nPlease set the required environment variables and try again.")
        print("\nExample:")
        print("  export AZURE_OPENAI_ENDPOINT='https://your-resource.openai.azure.com/'")
        print("  export AZURE_OPENAI_API_KEY='your-api-key'")
        print("  export AZURE_OPENAI_DEPLOYMENT_NAME='computer-use-preview'")
        return
    
    # Run the demo
    demo = ComputerUseDemo()
    demo.run_demo()


if __name__ == "__main__":
    main()
