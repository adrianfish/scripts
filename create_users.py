import requests

s = requests.Session()

r = s.get(f'http://127.0.0.1/api/login?username=admin&password=admin')

url = 'http://127.0.0.1/direct/user'

def create(user):
    r = s.post(url, data = user)

for num in range(5, 500):
    create({ 'eid': f'user{num}',
                'firstName' : 'User',
                'lastName': f'{num}', 
                'password': f'user{num}',
                'email': f'user{num}@mailinator.com'
            })
