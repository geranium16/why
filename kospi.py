import requests
from bs4 import BeautifulSoup
# bs4라는 곳에서 beautifulsoup을 불러올것임

url="https://finance.naver.com/sise/"

# request=requests.get(url)
request=requests.get(url).text
soup=BeautifulSoup(request,'html.parser')
# html파일을 파이썬이 읽을 수 있게 파싱
# print(soup)
kospi=soup.select_one("#KOSPI_now")
print(kospi.txt) 
# .txt붙이면 txt만 나온다