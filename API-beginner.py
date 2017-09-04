import requests
import json

f = input("Convert from : ")
f = f.upper()
t = input("Convert to : ")
t = t.upper()

parameters = {'base':f, 'symbols':t}
response = requests.get("http://api.fixer.io/latest", params = parameters)

status_code = response.status_code

if status_code == 200:

	# content = response.content
	# json_data = json.loads(content)

	# OR directly decode the json string to python object
	json_data = response.json()

	fromcurr = json_data['base']
	tocurr = list(json_data['rates'].keys())[0]
	rate = json_data['rates'][tocurr]
	dateofconv = json_data['date']
	print(f"The conervsation rate as of {dateofconv} from {fromcurr} to {tocurr} is {rate}")

else:
	print("Error in fetching data from API")