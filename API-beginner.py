import requests
import json

parameters = {'base':'USD', 'symbols':'INR'}
response = requests.get("http://api.fixer.io/latest", params = parameters)
status_code = response.status_code
print(status_code)
content = response.content
fromcurr = json.loads(content)['base']
tocurr = list(json.loads(content)['rates'].keys())[0]
rate = json.loads(content)['rates'][f'{tocurr}']
dateofconv = json.loads(content)['date']
print(f"The conervsation rate as of {dateofconv} from {fromcurr} to {tocurr} is {rate}")