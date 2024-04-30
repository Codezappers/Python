import requests
from pprint import pprint

API_KEY = 'bd5e378503939ddaee76f12ad7a97608'

city = input('Enter the city: ')
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

weather_data = requests.get(base_url).json()

pprint(weather_data)