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
    print(json_data)


if __name__ == "__main__":
    get_joke()
    # get_joke_by_category("programming")
