import requests

# Ollama local API URL
url = "http://localhost:11434/api/generate"

prompt = input("Enter your prompt: ")

data = {
    "model": "llama3",
    "prompt": prompt,
    "stream": False
}

try:
    response = requests.post(url, json=data)

    result = response.json()

    print("\nAI Response:\n")
    print(result["response"])

except Exception as e:
    print("Error occurred:", e)