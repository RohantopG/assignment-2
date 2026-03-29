import os
import requests
import sys

from dotenv import load_dotenv

def main():
    load_dotenv()
   
    api_key = os.environ.get("HUGGINGFACE") or os.environ.get("HUGGINGFACE_API_KEY")
    if not api_key:
        sys.exit("Please set the HUGGINGFACE key in the .env file.")

    prompt = input("Enter your prompt for Hugging Face: ")

    
    API_URL = "https://router.huggingface.co/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}"}

    data = {
        "model": "Qwen/Qwen2.5-72B-Instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 250
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        
        
       
        if "choices" in result and len(result["choices"]) > 0:
            print(result["choices"][0]["message"]["content"])
        else:
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
        if 'response' in locals() and hasattr(response, 'text'):
            print(f"Response content: {response.text}")

if __name__ == "__main__":
    main()
