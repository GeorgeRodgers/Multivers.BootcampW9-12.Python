# Occasionally we will need to install packages to add extra functionality to python
# requests is a http request package and is installed using the command 'pip install requests'
# Once downloaded you can import the request package

import requests

res = requests.get('http://api.open-notify.org/astros.json') #HTTP GET request saved to variable
data = res.json() # request response is not initially readable so I must be converted into the JSON format

print(data)

# We can just print the JSON data from the request
# It would be better to use a loop to get the just the names

print('\nThe people currently in space are:')
for i in data['people']: # The 'people' key is required to select the list stored in it's value
    print(i['name']) # The 'name' key is required to get the name