import requests
import json 

#이미지가 있는 image_url 을 통해 file_name 파일로 저장하는 함수

def save_image(image_url,file_name) :
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        
        with open(file_name,'wb') as fp :
            fp.write(img_response.content)


#이미지가 있는 url 주소
url = "https://dapi.kakao.com/v2/search/image"
headers = {
    'Authorization' : 'KakaoAK 14be2c1b24dc25611ce57d9f58bbcae6 '
}
data = {
    'query' : '펭수'
}
response = requests.post(url, headers=headers, data=data)
#해당 url로 서버에게 요청
if response.status_code != 200:
    print("error!because", response.json())
#요청에 성공했다면
else :
    count = 0 
    for image_info in response.json()['documents']:
        print(f'[{count}th) image_url = ', image_info ['image_url'])
        #저장될 이미지 파일명 설정
        count = count +1
        file_name = 'test_%d.jpg'%(count)

        save_image(image_info['image_url'], file_name)