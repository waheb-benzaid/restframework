import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint,json ={"query":"Hello World"})
print(get_response.text)