#!/usr/bin/env python3
"""
Setup verification script for GPT Computer Use Demo.
Run this to check if all dependencies are installed correctly.
"""

import sys
import os

def check_python_version():
    """Check if Python version is 3.8+"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (requires 3.8+)")
        return False

def check_packages():
    """Check if required packages are installed"""
    print("\nChecking required packages...")
    
    packages = {
        'openai': 'OpenAI Python SDK',
        'playwright': 'Playwright',
        'azure.identity': 'Azure Identity'
    }
    
    all_installed = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name}")
        except ImportError:
            print(f"✗ {name} (not installed)")
            all_installed = False
    
    return all_installed

def check_playwright_browsers():
    """Check if Playwright browsers are installed"""
    print("\nChecking Playwright browsers...")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(headless=True)
                browser.close()
                print("✓ Chromium browser")
                return True
            except Exception as e:
                print(f"✗ Chromium browser (not installed)")
                print(f"  Run: playwright install chromium")
                return False
    except ImportError:
        print("✗ Cannot check (playwright not installed)")
        return False

def check_environment_variables():
    """Check if required environment variables are set"""
    print("\nChecking environment variables...")
    
    required_vars = {
        'AZURE_OPENAI_ENDPOINT': False,
        'AZURE_OPENAI_API_KEY': False,
        'AZURE_OPENAI_DEPLOYMENT_NAME': False
    }
    
    all_set = True
    for var in required_vars:
        if os.getenv(var):
            print(f"✓ {var}")
        else:
            print(f"⚠ {var} (not set)")
            all_set = False
    
    if not all_set:
        print("\n  Note: Environment variables can be set via .env file or shell exports")
        print("  See .env.example for reference")
    
    return all_set

def main():
    """Run all checks"""
    print("="*60)
    print("GPT Computer Use Demo - Setup Verification")
    print("="*60 + "\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Python Packages", check_packages),
        ("Playwright Browsers", check_playwright_browsers),
        ("Environment Variables", check_environment_variables)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"Error in {name}: {e}")
            results.append((name, False))
    
    print("\n" + "="*60)
    print("Verification Summary")
    print("="*60)
    
    critical_passed = True
    optional_passed = True
    
    for i, (name, result) in enumerate(results):
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        
        # Environment variables are optional for setup check
        if name == "Environment Variables":
            if not result:
                status = "WARN"
                symbol = "⚠"
                optional_passed = False
            print(f"{symbol} {name}: {status}")
        else:
            print(f"{symbol} {name}: {status}")
            if not result:
                critical_passed = False
    
    print("="*60)
    
    if critical_passed:
        print("\n✓ All critical checks passed!")
        if optional_passed:
            print("✓ Environment variables are set - you're ready to run the demo!")
        else:
            print("⚠ Remember to set environment variables before running the demo.")
        print("\nRun the demo with: python app.py")
        return 0
    else:
        print("\n✗ Some critical checks failed. Please install missing dependencies:")
        print("\n  pip install -r requirements.txt")
        print("  playwright install chromium")
        return 1

if __name__ == "__main__":
    sys.exit(main())
