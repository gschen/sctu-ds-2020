import requests
from bs4 import BeautifulSoup
import re


def getHtml(url):
    try:
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
    except:
        "wrong"
def getID(url):
    try:
        list1 = []
        r = requests.get(url)
        r.status_code
        r.raise_for_status
        r.encoding = 'utf-8'
        html = r.text
        soup = BeautifulSoup(html,"html.parser")
        links = soup.find(class_="content-img-list")
        links1 = links.find_all("a")
        if list1 != []:
            list1 = []
        for i in links1:
            list1.append(i.get("href"))
        return list1[0:12]
    except:
        "wrong"
def get_movie_details(url):
    try:
        r = requests.get(url)
        r.status_code
        r.raise_for_status
        r.encoding = 'utf-8'
        html = r.text
        soup = BeautifulSoup(html,"html.parser")
        soup.prettify()
        s = soup.find(class_="text-list").get_text()
        print(s)
    except:
        "wrong"



def main(url):
    start_url = getHtml(url)
    for i in range(1,233):
        category = start_url+"&page={}".format(i)
        movie = getID(category)
        for ids in movie:
            items = get_movie_details(url+'{}'.format(ids))
            item_list.append(ids)
        

    

if __name__ =="__main__":
    url = "http://www.emdy.cn/"
    item_list = []
    main(url)
