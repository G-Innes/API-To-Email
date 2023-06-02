import requests
import random


# calls the API and selects a random choice from the response & returns content to be sent to the users email
def meme_api(api_key):
    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "programming-memes-images.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers)

    memes = response.json()
    meme = random.choice(memes)
    content = meme["image"]
    return content
