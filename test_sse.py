import pprint
import requests
import sseclient
import json

s = requests.Session()

r = s.get('http://127.0.0.1/api/login?username=user1&password=user1')

url = 'http://127.0.0.1/api/users/me/events'
headers = {'Accept': 'text/event-stream'}
r = s.get(url, stream=True, headers=headers)
client = sseclient.SSEClient(r)
for event in client.events():
    pprint.pprint(json.loads(event.data))
