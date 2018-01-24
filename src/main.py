import requests
import json

API = "http://192.168.10.124/api/KLLqzTPwMccLtPjeNypu7ktiLnf811tGKpSKZAlY/lights"



LIGHTS = requests.get(API)
print(LIGHTS)
print(LIGHTS.text)


TURN_ON = json.dumps({"on":True})

print(TURN_ON)
RESPONSE = requests.put(API + "/1/state", data=TURN_ON)


print(RESPONSE.text)


