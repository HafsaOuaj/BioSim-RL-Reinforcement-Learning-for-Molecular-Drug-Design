import requests

# Example: search aspirin
response = requests.get('http://zinc15.docking.org/substances?search=aspirin')
data = response.json()

print(data)


