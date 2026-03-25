import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Setup
load_dotenv()
api_key = os.getenv("HF_API_KEY")

if not api_key:
    print("Error: HF_API_KEY not found in .env")
    exit()

# 2. Initialize Client with Llama 3.2 (The most stable 2026 model)
client = InferenceClient(token=api_key)
MODEL_ID = "meta-llama/Llama-3.2-1B-Instruct"

def ask_ai():
    prompt = input("Enter your prompt: ")
    print("\nProcessing request...")

    try:
        # Using the standard chat_completion which is the primary 2026 path
        response = client.chat_completion(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        
        print("\n--- AI Response ---")
        print(response.choices[0].message.content.strip())

    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    ask_ai()