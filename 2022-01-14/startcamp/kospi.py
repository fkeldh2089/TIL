import requests
addr='https://finance.naver.com/sise/'
a=requests.get(addr).text

from bs4 import BeautifulSoup

data = BeautifulSoup(a,'html.parser')

kospi = data.select_one('#KOSPI_now')

print(kospi.text)

