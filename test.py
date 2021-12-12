import requests


url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'https://raw.githubusercontent.com/Phunbie/assignments/main/610968546.jpg'}

result = requests.post(url, json=data).json()
print(result)