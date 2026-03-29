import os
import sys
try:
    from groq import Groq
except ImportError:
    sys.exit("Please install groq package: pip install groq")

from dotenv import load_dotenv

def main():
    load_dotenv()
  
    api_key = os.environ.get("GROKAI") or os.environ.get("GROQ_API_KEY")
    if not api_key:
        sys.exit("Please set the GROKAI or GROQ_API_KEY in the .env file.")

    client = Groq(api_key=api_key)

    prompt = input("Enter your prompt for Groq: ")

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.1-8b-instant",
        )
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
