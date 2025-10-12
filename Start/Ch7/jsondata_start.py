# LinkedIn Learning Python course by Joe Marini
# Example file for parsing and processing JSON
#

import urllib.request 
import json

# Open the URL and read the data
web_url = urllib.request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")

# Read the JSON data from the source

data = web_url.read()
# print(web_url.getcode())
# print(data)

# Print the content of the 'text' field
theJSON = json.loads(data)
print(theJSON["text"])