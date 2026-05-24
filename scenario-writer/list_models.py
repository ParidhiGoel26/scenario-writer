from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    client = genai.Client(api_key=api_key)
    
    # List available models
    print("Available models:")
    for model in client.models.list():
        print(f"  - {model.name}")
else:
    print("No API key found")