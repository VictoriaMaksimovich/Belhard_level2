import requests


def get_duck():
    url = 'https://random-d.uk/api/v2/random'
    res_duck = requests.get(url).json()
    return res_duck['url']


def get_fox():
    url = 'https://randomfox.ca/floof/'
    res_fox = requests.get(url).json()
    return res_fox['image']


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'APPID': 'd0badf68b676f6f0ce6f13bdbccbf5b8'}
    res = requests.get(url, params).json()
    return res



