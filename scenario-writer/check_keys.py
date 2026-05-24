import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("Checking your API Keys")
print("=" * 50)

openai_key = os.getenv("OPENAI_API_KEY")
groq_key = os.getenv("GROQ_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")
huggingface_key = os.getenv("HUGGINGFACE_API_KEY")

print(f"\nOPENAI_API_KEY: {'✅ Found' if openai_key else '❌ Not found'}")
if openai_key:
    print(f"   Starts with: {openai_key[:10]}...")

print(f"\nGROQ_API_KEY: {'✅ Found' if groq_key else '❌ Not found'}")
if groq_key:
    print(f"   Starts with: {groq_key[:10]}...")

print(f"\nGEMINI_API_KEY: {'✅ Found' if gemini_key else '❌ Not found'}")
if gemini_key:
    print(f"   Starts with: {gemini_key[:10]}...")

print(f"\nHUGGINGFACE_API_KEY: {'✅ Found' if huggingface_key else '❌ Not found'}")
if huggingface_key:
    print(f"   Starts with: {huggingface_key[:10]}...")

print("\n" + "=" * 50)

if not any([openai_key, groq_key, gemini_key, huggingface_key]):
    print("\n⚠️ No API keys found!")
    print("\nYou have two options:")
    print("1. Add an API key to .env file")
    print("2. Continue with intelligent fallback (still works, just not real AI)")
else:
    print("\n✅ You have API keys! The AI will work!")