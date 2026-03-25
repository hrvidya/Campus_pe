import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found.")
    exit()

# Configure Gemini
genai.configure(api_key=api_key)

# Take input
prompt = input("Enter your prompt: ")

try:
    # ✅ Use latest working model
    model = genai.GenerativeModel("gemini-2.0-flash")

    response = model.generate_content(prompt)

    print("\nAI Response:\n")
    print(response.text)

except Exception as e:
    print("Error occurred:", e)