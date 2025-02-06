import requests
import json

from utilities.readProperties import ReadConfig

# API Endpoint
baseURL = ReadConfig.getApiUrl()
api = baseURL+ "/v1/bpi/currentprice.json"

response = requests.get(api)
assert response.status_code == 200
data = response.json()

print(data)

bpid_key = data['bpi'].keys()
expected_bpi = {'USD', 'GBP', 'EUR'}

try:
    assert expected_bpi.issubset(bpid_key)
    assert data['bpi']['GBP']['description'] == "British Pound Sterling1122"
    print("Test Passed: API response is valid")

except:
    print("Test Failed")