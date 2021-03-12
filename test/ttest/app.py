import requests
from bs4 import BeautifulSoup

def handler(event, context):
    url = 'https://search.naver.com/search.naver?&where=news&query=%EB%A9%94%EA%B0%80%EC%A1%B4%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('ul.list_news')
        print(ul)
        return "ok"
        
    else:
        print(response.status_code)
        return "fail"

