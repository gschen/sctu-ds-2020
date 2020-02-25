import requests
from bs4 import BeautifulSoup
import re


def getHtml(url):
    r = requests.get(url,timeout = 30)
    r.status_code
    r.raise_for_status
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find(class_="nav navbar-nav li_m-l-4")
    link = links.find_all("a")
    s = link[5]
    h = s.get("href")
    return url+h
def getID(url):
    r = requests.get(url)
    r.status_code
    r.raise_for_status
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    links = soup.find(class_="content-img-list")
    links1 = links.find_all("a")
    for i in links1:
        list1.append(i.get("href"))
    return list1
def get_movie_details(url):
    r = requests.get(url)
    r.status_code
    r.raise_for_status
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    soup.prettify()
    s = soup.find(class_="text-list").get_text()
    print(s)



def main(url):
    start_url = getHtml(url)
    for i in range(1,233):
        category = start_url+"&page={}".format(i)
        movie = getID(category)
        for ids in movie:
            items = get_movie_details(url1+"{}".format(ids))
            item_list.append(items)

    

if __name__ =="__main__":
    url = "http://www.emdy.cn/"
    url1 = "http://www.emdy.cn"
    list1 = []
    item_list = []
    main(url) 
    