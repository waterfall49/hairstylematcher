''' from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation


arguments = {"keywords":"문채원, 전지현, 크리스탈, 윤아, 웬디, 한지민, 김고은, 휘인, 고준희, 김지원, 혜리, 수영, 서현진, 강미나, 황정음, 김나영, 가희, 장도연, 정유미, 조이, 박보영, 공효진, 유라, 현아",
"limit":50,"print_urls":True, "format": "jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images '''

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
# 한글 검색 자동 변환
url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img', limit=30)
# print(img)

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('./img/' + plusUrl + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
print('다운로드 완료')