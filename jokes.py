import requests
import json


def printDataDictionaryVise(json_dt):
    joke_id = json_dt["id"]
    joke_type = json_dt["type"]
    joke_setup = json_dt["setup"]
    joke_punchline = json_dt["punchline"]
    print(joke_id)
    print(joke_type)
    print(joke_setup)
    print(joke_punchline)


def get_joke():
    api_end_point = "https://official-joke-api.appspot.com/jokes/random"
    joke = requests.get(api_end_point)
    json_data = json.loads(joke.text)
    printDataDictionaryVise(json_data)


def get_joke_by_category(category):
    api_end_point = "https://official-joke-api.appspot.com/jokes/"+category+"/random"
    joke = requests.get(api_end_point)
    json_data = json.loads(joke.text)
    printDataDictionaryVise(json_data)


def newJokeApi():
    api_end_point = "https://api.chucknorris.io/jokes/random"
    joke = requests.get(api_end_point)
    json_data = json.loads(joke.text)
    joke_category = json_data["categories"]
    joke_created_at = json_data["created_at"]
    joke_icon_url = json_data["icon_url"]
    joke_id = json_data["id"]
    joke_updated_at = json_data["updated_at"]
    joke_url = json_data["url"]
    joke_value = json_data["value"]

    print(json_data)
    print(joke_category)
    print(joke_created_at)
    print(joke_icon_url)
    print(joke_id)
    print(joke_updated_at)
    print(joke_url)
    print(joke_value)


if __name__ == "__main__":
    # get_joke()
    # get_joke_by_category("programming")
    newJokeApi()


# categories , created_at , icon_url, id, updated_at ,url , value,
