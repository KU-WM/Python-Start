import requests

try:
    response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities")
    if response.status_code == 200:
        print(response.content)
    else:
        print("Connection Error", response.status_code, response.content)
except Exception as e:
    print(e)