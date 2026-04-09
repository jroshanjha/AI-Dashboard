import requests

async def analyze_image(file):
    image_bytes = await file.read()

    response = requests.post(
        "https://api.deepai.org/api/image-recognition",
        files={'image': image_bytes},
        headers={'api-key': 'YOUR_FREE_API_KEY'}
    )

    return response.json()