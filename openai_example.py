import os
import sys
try:
    from openai import OpenAI
except ImportError:
    sys.exit("Please install openai package: pip install openai")

from dotenv import load_dotenv

def main():
    load_dotenv()
    
    api_key = os.environ.get("CHATGPT") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("Please set the CHATGPT or OPENAI_API_KEY in the .env file.")

    client = OpenAI(api_key=api_key)

    prompt = input("Enter your prompt for OpenAI: ")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        print("\n--- OpenAI Response ---")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
