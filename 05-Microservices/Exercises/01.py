import requests

from pprint import pprint
from datetime import datetime


url = 'https://api.zippopotam.us/{region_code}/{postal_code}'

region_code = input("\nInsert region code: ")
postal_code = input("\nInsert postal code: ")

response = requests.get(url=url.format(region_code=region_code, postal_code=postal_code))

try:
    response.raise_for_status()
    locations = response.json()

    print(f"\nLocations associated to postal code {locations['post code']} in {locations['country']}:")
    for location in locations['places']:
        print(f"\nPlace name: {location['place name']}")
        print(f"State name: {location['state']}")
        print(f"Latitude  : {location['latitude']}")
        print(f"Longitude : {location['longitude']}")

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code} - {response.reason}")

except requests.exceptions.JSONDecodeError:
    print(f"Error while decoding response as JSON.")

print()


################################################################################



url = "https://api.apilayer.com/exchangerates_data/symbols"

headers = {
    'ApiKey': '00000000000000000000000000000000',
    'Content-Type': 'application/json'
}

response = requests.get(url=url, headers=headers, timeout=15)

try:
    response.raise_for_status()
    symbols = response.json()
    
    print("List of symbols:")
    for symbol, description in symbols['symbols'].items():
        print(">", symbol, "-", description)

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code} - {response.reason}")

except requests.exceptions.JSONDecodeError:
    print(f"Error while decoding response as JSON.")


################################################################################


url = "https://api.apilayer.com/exchangerates_data/convert"

params = {
    'amount': '{a}',
    'from': '{f}',
    'to': '{t}'
}

headers = {
    'ApiKey': '00000000000000000000000000000000',
    'Content-Type': 'application/json'
}

currency_amount = input('Enter currency amount to convert: ')
currency_from = input('Enter currency symbol to convert from: ')
currency_to = input('Enter currency symbol to convert to: ')

response = requests.get(url=url, params={k: v.format(a=currency_amount, f=currency_from, t=currency_to) for k, v in params.items()}, headers=headers, timeout=15)

try:
    response.raise_for_status()
    conversion = response.json()
    
    # pprint(conversion)

    print(f"Date rate:  {conversion['date']} ({conversion['info']['timestamp']})")
    print(f"Conversion: {conversion['query']['from']} {conversion['query']['amount']:.2f} = {conversion['query']['to']} {conversion['result']:.2f}")

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code} - {response.reason}")

except requests.exceptions.JSONDecodeError:
    print(f"Error while decoding response as JSON.")


################################################################################


url = "https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"

headers = {
    'X-ClientId': '00000000-0000-0000-0000-000000000000',
    'passKey': '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
    'Content-Type': 'application/json'
}

request = requests.get(url=url, headers=headers)

try:
    request.raise_for_status()
    request_json = request.json()
    access_token = request_json['data'][0]['accessToken']
    pprint(request_json)

except requests.exceptions.HTTPError:
    print(f"HTTP error: {request.status_code} - {request.reason}")

except requests.exceptions.JSONDecodeError:
    print(f"Error while decoding response as JSON.")


################################################################################


url = "https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/{stop_id}/arrives/"

headers = {
    'accessToken': access_token,
    'Content-Type': 'application/json'
}

body = {
    "cultureInfo": "ES",
    "Text_StopRequired_YN": "Y",
    "Text_EstimationsRequired_YN": "Y",
    "Text_IncidencesRequired_YN": "Y",
    "DateTime_Referenced_Incidencies_YYYYMMDD": datetime.now().strftime('%Y%m%d')
}

stop_id = input("Enter stop ID: ")

response = requests.post(url=url.format(stop_id=stop_id), headers=headers, json=body)

try:
    response.raise_for_status()
    stop_detail = response.json()
    
    pprint(stop_detail)

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code} - {response.reason}")

except requests.exceptions.JSONDecodeError:
    print(f"Error while decoding response as JSON.")


################################################################################


url = "https://openapi.emtmadrid.es/v2/citymad/places/parkings/availability/"

response = requests.get(url=url, headers=headers)

try:
    response.raise_for_status()
    parkings = response.json()

    availables = list(filter(lambda x: isinstance(x['freeParking'], int) and x['freeParking'] > 0, parkings['data']))

    print("Parkings available:")
    # [print(f" * {available['name']} ({available['address']}) - Available: {available['freeParking']}") for available in availables]
    [print(f" * Available: {available['freeParking']:>4d} - Parking: {available['name']} [{available['address']}]") for available in availables]
    # print(f"Total free: {sum(available['freeParking'] for available in availables):>6d}")
    print(f"Total free: {sum(map(lambda x: x['freeParking'], availables)):>6d}")

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code} - {response.reason}")

except requests.exceptions.JSONDecodeError:
    print(f"Error while decoding response as JSON.")


################################################################################


url = "https://openapi.emtmadrid.es/v1/mobilitylabs/user/logout/"

response = requests.get(url=url, headers=headers)

try:
    response.raise_for_status()
    response_json = response.json()
    
    pprint(response_json)

except requests.exceptions.HTTPError:
    print(f"HTTP error: {response.status_code} - {response.reason}")

except requests.exceptions.JSONDecodeError:
    print(f"Error while decoding response as JSON.")
