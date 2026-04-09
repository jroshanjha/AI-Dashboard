import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def process_text(text):
    response = requests.post(API_URL, json={"inputs": text})
    return response.json()