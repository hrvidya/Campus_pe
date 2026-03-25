import os
from dotenv import load_dotenv
import cohere

load_dotenv()

def main():
    api_key = os.getenv("COHERE_API_KEY")

    if not api_key:
        print("\n[!] ERROR: COHERE_API_KEY not found in .env file.")
        return

    try:
        co = cohere.ClientV2(api_key=api_key)

        prompt = input("\nEnter your prompt for Cohere: ")

        print("\nConnecting to Cohere...\n")

        response = co.chat(
            model="command-a-03-2025",   # ✅ Updated working model
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print("Cohere Response:\n")
        print(response.message.content[0].text)

        print("\n" + "-" * 40)

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("If error continues, update library:")
        print("pip install -U cohere")


if __name__ == "__main__":
    main()