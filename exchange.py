import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/marketindex/"

# get 방식으로 url의 내용을 text형식으로 request로 가져올거다.
request=requests.get(url).text
# 이를 python이 읽을 수 있게 가져온다.
soup=BeautifulSoup(request,'html.parser')

# html파일을 파이썬이 읽을 수 있게 파싱
# print(soup)
# 크롤링 : 사이트에서 찍고 select 뽑기
exchange=soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")
print(exchange.text) 