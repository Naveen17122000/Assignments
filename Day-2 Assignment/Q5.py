# Q5. Write a Python program using the request s module to send a GET request to a Given Below Url API endpoint and print the
# a)	latitude
# b)	longitude
# c)	timestamp

# (Url : http://api open-notify.org/iss-now.json)

import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
print("Status Code: ", response.status_code)

if response.status_code == 200:
    data = response.json()

    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    timestamp = data["timestamp"]

    print("Latitude : ", latitude)
    print("Lonfitude : ", longitude)
    print("Timestamp : ", timestamp)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
