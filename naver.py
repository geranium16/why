import requests
from bs4 import BeautifulSoup

url="https://www.naver.com/"
request=requests.get(url).text
soup=BeautifulSoup(request,'html.parser')


temp=soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul> li > a > span.ah_k")
# 리스트라서 텍스트로 변환할 수 없다.
#   ul> li:nth-child(3) > a > span.ah_k 에서 nth-child(3)을 지우면 모든 li의 a의 span으로 들어간다 
# 또한 이를 통해 여러번 자료를 받아 올것이니 list이다.
for i in temp : 
  print(i.text)
