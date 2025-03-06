# pip install requestㅌ

# venv를 만들어 가상환경을 설정할 수 있다.
# 가상환경 내부에서는 pip install할 수 없다.

import requests

response = requests.get("http://api.github.com")
print(response.content.decode("utf-8"))

response = requests.get("https://www.naver.com")
print(type(response.content))
