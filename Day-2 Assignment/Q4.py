# Q4. Write a Python program using the request s module to send a GET request to a Given Below UrIAPI endpoint and print the JSON response
# (Url : http://api.open-notify.org/iss-now.json)

import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
print(response)
if response.status_code == 200:

    data = response.json()
    print("JSON Response")
    print(data)

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
