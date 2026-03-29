import os
import sys
import cohere
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("COHERE") or os.environ.get("COHERE_API_KEY")
if not api_key:
    sys.exit("Please set the COHERE key in the .env file.")

co = cohere.Client(api_key)

try:
    prompt = input("Enter your prompt for Cohere: ")

    response = co.chat(
        model="c4ai-aya-expanse-32b",   
        message=prompt
    )

    print("Response:", response.text)

except Exception as e:
    print("An error occurred:", e)