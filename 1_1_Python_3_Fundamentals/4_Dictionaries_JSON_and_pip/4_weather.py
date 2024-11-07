# The code below is used to securely stored the API key
import os
from dotenv import load_dotenv

def load_api_keys():
    load_dotenv()

load_api_keys()

# Imports requests package
import requests

# The original URL features the place name
# By breaking up the URL and replacing the place with a variable we can allow the user to input the place

place = input('Where would you like to know the weather for?\n')

# The URL is the saved as a variable

url = 'http://api.weatherapi.com/v1/current.json?key=' + os.getenv("API_KEY") + '&q=' + place + '&aqi=no'

# Using the request package we can get information from the api and store this in a variable

info = requests.get(url)

print('\n', info, '\n')

# The info variable does not give any useful information when printed
# Using the .json() function we can convert the information into a JSON format and store it in another variable

weather = info.json()
print('\n', weather, '\n')

# Now the new variable gives us too much information featuring nested dictionaries

# Using the .get() function we can retrieve select information from these dictionaries and store these as variables

temp = weather.get('current').get('temp_c')
condition = weather.get('current').get('condition').get('text')

# We can print the information in a logical sentence
print("Today's weather in", place, 'is',condition, 'and', temp, '°C.')