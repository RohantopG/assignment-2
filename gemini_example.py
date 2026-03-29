import os
import sys
try:
    import google.generativeai as genai
except ImportError:
    sys.exit("Please install google-generativeai package: pip install google-generativeai")

from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Please set the GEMINI key in the .env file.")

    genai.configure(api_key=api_key)

    prompt = input("Enter your prompt for Gemini: ") 


    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        print("\n ")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
