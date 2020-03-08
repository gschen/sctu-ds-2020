import requests
from bs4 import BeautifulSoup
import re
list3 = []
url = "http://www.emdy.cn/page.aspx?id=620&classid=3"

def get_movie_details(url):
    r = requests.get(url)
    r.status_code
    r.raise_for_status
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    soup.prettify()
    j = '<li>.*?</li>'
    s = re.compile(j)
    f = re.findall(s,soup.decode("utf-8"))
    return s
print(get_movie_details(url))
    
