import requests
import sys
import os

from dotenv import load_dotenv

def main():
    load_dotenv()
    
    url = "https://ollama.com/api/generate"
    api_key = os.environ.get("OLLAMA")
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    
    prompt = input("Enter your prompt for Ollama: ")
    data = {
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        result = response.json()
        print("\n--- Ollama Response ---")
        print(result.get("response", ""))
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Make sure the Ollama app is running locally on port 11434.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
