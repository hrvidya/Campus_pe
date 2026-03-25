from dotenv import load_dotenv
import os
from groq import Groq

# Load .env file
load_dotenv(dotenv_path=".env")

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Check if key exists
if not api_key:
    print("Error: GROQ_API_KEY not found. Check your .env file.")
    exit()

# Initialize Groq client
client = Groq(api_key=api_key)

# Take user input
prompt = input("Enter your prompt: ")

try:
    # Send request using updated model
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    # Print only AI response (no API key shown)
    print("\nAI Response:\n")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error occurred:", e)