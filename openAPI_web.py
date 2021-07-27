import requests
import json
url = "https://dapi.kakao.com/v2/search/web"
queryString = {'query' : '이효리'}
header = {'Authorization': 'KakaoAK 14be2c1b24dc25611ce57d9f58bbcae6'}
response = requests.get(url, headers=header, params=queryString)
tokens = response.json()
print(response)
print(tokens)