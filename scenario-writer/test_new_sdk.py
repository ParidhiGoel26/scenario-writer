import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print(f"API Key found: {'Yes' if api_key else 'No'}")

if api_key:
    # Import the new SDK correctly
    from google import genai
    
    # Create client
    client = genai.Client(api_key=api_key)
    
    # Test the API
    response = client.models.generate_content(
        model='gemini-2.0-flash-exp',
        contents="Say 'API is working with new SDK'"
    )
    
    print(f"Response: {response.text}")
    print("✅ New SDK is working perfectly!")
else:
    print("❌ No API key found in .env file")