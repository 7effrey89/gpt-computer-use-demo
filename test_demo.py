"""
Test script to validate the demo structure without requiring Azure credentials.
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported."""
    print("Testing imports...")
    
    try:
        import base64
        print("✓ base64")
    except ImportError as e:
        print(f"✗ base64: {e}")
        return False
    
    try:
        import json
        print("✓ json")
    except ImportError as e:
        print(f"✗ json: {e}")
        return False
    
    # Test that the demo module can be imported
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        # We'll just check if the file exists and can be parsed
            with open('app.py', 'r') as f:
            code = f.read()
                compile(code, 'app.py', 'exec')
        print("✓ demo.py (syntax valid)")
    except Exception as e:
            print(f"✗ app.py: {e}")
        return False
    
    return True

def test_file_structure():
    """Test that all required files exist."""
    print("\nTesting file structure...")
    
    required_files = [
            'app.py',
        'requirements.txt',
        '.env.example',
        '.gitignore',
        'README.md'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"✓ {file}")
        else:
            print(f"✗ {file} (missing)")
            all_exist = False
    
    return all_exist

def test_requirements():
    """Test that requirements.txt has the necessary packages."""
    print("\nTesting requirements.txt...")
    
    with open('requirements.txt', 'r') as f:
        requirements = f.read()
    
    required_packages = ['openai', 'playwright', 'azure-identity']
    all_present = True
    
    for package in required_packages:
        if package in requirements:
            print(f"✓ {package}")
        else:
            print(f"✗ {package} (missing)")
            all_present = False
    
    return all_present

def test_env_example():
    """Test that .env.example has the necessary variables."""
    print("\nTesting .env.example...")
    
    with open('.env.example', 'r') as f:
        env_content = f.read()
    
    required_vars = [
        'AZURE_OPENAI_ENDPOINT',
        'AZURE_OPENAI_API_KEY',
        'AZURE_OPENAI_DEPLOYMENT_NAME'
    ]
    
    all_present = True
    for var in required_vars:
        if var in env_content:
            print(f"✓ {var}")
        else:
            print(f"✗ {var} (missing)")
            all_present = False
    
    return all_present

def test_demo_class():
    """Test that the demo script has the expected structure."""
    print("\nTesting demo.py structure...")
    
        with open('app.py', 'r') as f:
        demo_content = f.read()
    
    expected_elements = [
        'class ComputerUseDemo',
        'def start_browser',
        'def take_screenshot',
        'def get_computer_use_action',
        'def summarize_content',
        'def navigate_to_page',
        'def click_navigation_item',
        'def run_demo',
        'Identity Support',
        'Throttling'
    ]
    
    all_present = True
    for element in expected_elements:
        if element in demo_content:
            print(f"✓ {element}")
        else:
            print(f"✗ {element} (missing)")
            all_present = False
    
    return all_present

def main():
    """Run all tests."""
    print("="*60)
    print("Running validation tests for GPT Computer Use Demo")
    print("="*60)
    
    tests = [
        ("Import Tests", test_imports),
        ("File Structure", test_file_structure),
        ("Requirements", test_requirements),
        ("Environment Example", test_env_example),
        ("Demo Structure", test_demo_class)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\nError in {name}: {e}")
            results.append((name, False))
    
    print("\n" + "="*60)
    print("Test Results Summary")
    print("="*60)
    
    all_passed = True
    for name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "✓" if result else "✗"
        print(f"{symbol} {name}: {status}")
        if not result:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n✓ All tests passed!")
        return 0
    else:
        print("\n✗ Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
