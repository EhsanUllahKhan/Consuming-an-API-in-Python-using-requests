import requests
import json

def get_joke():
    api_end_point = "https://official-joke-api.appspot.com/jokes/random"
    joke = requests.get(api_end_point)
    json_data = json.loads(joke.text)
    print(json_data)


if __name__ == "__main__":
    get_joke()