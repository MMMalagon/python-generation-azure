import requests

from pprint import pprint

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

print(response.status_code, '-', response.reason)

'''
try:
    response.raise_for_status()
    pprint(response.content)
    pprint(response.json())
except requests.exceptions.HTTPError:
    print("Not-OK")
except requests.exceptions.JSONDecodeError:
    print("Not JSON")
'''

if response.status_code == 200:
    print("Headers:          ", response.headers)
    print("Content-Type:     ", response.headers.get('Content-Type'))
    print("Content-Length:   ", response.headers.get('Content-Length'), "bytes")
    print("Content (bytes):  ", response.content)
    print("Content (decoded):", response.text)
    
    if response.headers.get('Content-Type') == 'application/json':
        data = response.json()
        print("Message:          ", data.get('message'))
        print("Timestamp:        ", data.get('timestamp'))
        print("Latitude:         ", data.get('iss_position').get('latitude'))
        print("Longitude:        ", data.get('iss_position').get('longitude'))
else:
    print("Data processing error")


################################################################################


url = 'https://postman-echo.com/post'

headers = {
    'Content-Type': 'application/json',
    'Api-Key': '00000000000000000000000000000000'
}

params = {
    'id': 100,
    'process': 'orders'
}

data = {
    'id': 100,
    'process': 'orders'
}

response = requests.request('POST', url=url, params=params, headers=headers, data=data)

print(response.status_code, '-', response.reason)
print("Headers:          ", response.headers)
print("Content (decoded):", response.text)
