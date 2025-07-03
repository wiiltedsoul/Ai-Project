import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("No input provided. Please provide a prompt as a command line argument.")
    exit(1)

user_prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages
)
if "--verbose" in sys.argv:
    if response.usage_metadata:
            print(response.text)
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)