import pprint
import requests
import sseclient
import json
import threading

def connect(username, password):

    s = requests.Session()

    r = s.get(f'http://127.0.0.1/api/login?username={username}&password={password}')

    url = 'http://127.0.0.1/api/users/me/events'
    headers = {'Accept': 'text/event-stream'}
    r = s.get(url, stream=True, headers=headers)
    client = sseclient.SSEClient(r)
    for event in client.events():
        pprint.pprint(json.loads(event.data))

for num in range(1, 100):
    x = threading.Thread(target=connect, args=(f'user{num}', f'user{num}'))
    x.start()

