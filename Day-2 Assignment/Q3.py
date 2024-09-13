# Q3 Write a Python program that reads a JSON file containing NASA APOD data and prints the keys : “expIanation","TitIe"
# Use this link to copy your json data (do not use request module , just save the Json to a variable then do json operation)
# JSON Data url : https://api.nasa.gov/planetary/apod?api key=DEMO KEY

import json

nasa_apod_data = '''
{
"date" : "12/09/24",
"explanation" : "NASA's Astronomy Picture of the Day (APOD) shares interesting facts about the universe, offering insights into astronomy and astrophysics.",
"title" : "Exploring the Cosmos",
"media_type" : "text",
"service_version" : "v1"
}'''

data = json.loads(nasa_apod_data)

print("Title :", data["title"])
print("Explaination :", data["explanation"])
