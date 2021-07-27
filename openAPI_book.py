import requests
import json
 
url = "https://dapi.kakao.com/v3/search/book"

data = {'query' : '미움받을 용기'}
header = {'Authorization' : 'KakaoAk 14be2c1b24dc25611ce57d9f58bbcae6'}

response = requests.post(url, headers=header, data=data)


print(response)
