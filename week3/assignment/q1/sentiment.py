import httpx

# Define the API endpoint and dummy API key
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer dummy-api-key"  # Dummy key
}

# Construct the message payload
payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "system",
            "content": "You are a sentiment analysis assistant. Classify the sentiment of the given text strictly as GOOD, BAD, or NEUTRAL."
        },
        {
            "role": "user",
            "content": "w  vd P2 DjQC tI 9oGBK0PyW 1DQfrT gKacM92ANHKnG7lP"
        }
    ]
}

# Send the POST request
response = httpx.post(url, json=payload, headers=headers)
response.raise_for_status()  # Ensure the request succeeded

# Parse and print the response JSON
data = response.json()
print(data)
