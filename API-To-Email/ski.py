import requests


# Ski calls the API and unpacks relevant info to variables and returns all as content for use in Main
# This returns select amount of info from the API about a ski resort to be sent to the users email address
def ski_api(api_key):
    url = (
        "https://ski-resorts-and-conditions.p.rapidapi.com/v1/resort/whistler-blackcomb"
    )

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "ski-resorts-and-conditions.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers)

    name = response.json()["data"]["name"]
    website = response.json()["data"]["href"]

    user = response.json()["data"]["twitter"]["user"]
    tweets = response.json()["data"]["twitter"]["tweets"]

    conditions = response.json()["data"]["conditions"]
    lift_status = response.json()["data"]["lifts"]["status"]

    content = name, website, conditions, lift_status, user, tweets

    return content
