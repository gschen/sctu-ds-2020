import requests
import json
from bs4 import BeautifulSoup

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}
# file = open(r"C:\Users\LEGION\Desktop\meituan.txt","w",newline ='',encoding='utf-8') 
url='https://www.meituan.com/meishi/162933409'
def get_all(urls):
    html= requests.get(urls,headers = hd).text
    print(html)
    soup = BeautifulSoup(html,'html.parser')
    shopname=soup.find('div',class_="title").text()
    return shopname
print(get_all(url))