import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        return r.text
    except:
        return "解析网页出错"

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,"html.parser")
    a = soup.find_all("a")
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue
    return lst


def getStockInfo(lst,stockURL,fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "" or html == None:
                continue
            l=[]
            soup = BeautifulSoup(html,"html.parser")
            stockInfo = soup.find("table",attrs={'class':'quote'})
            trans = str(stockInfo)
            reg = r'<td>(.*?)</td>'
            texty = re.compile(reg)
            s1 = re.findall(texty,trans)[1::]
            reg1 = r'<td>(.*?)<a'
            texty1 = re.compile(reg1)
            s2 = re.findall(texty1,trans)[0]
            for i in s1:
                s = i.replace("\u3000","")
                x = s.replace("<span style=\"color:rgb(0,102,0)\">","")
                b = x.replace("<span style=\"color:rgb(0,0,0)\">","")
                a = b.replace("</span>","")
                c = a.replace("<span style=\"color:rgb(255,0,0)\">","")
                l.append(c)
            w = ",".join(l)
            if l == []:
                continue
                
            with open(fpath,'a',encoding = 'utf-8') as f:
                f.write(s2+'\u3000')
                f.write(w+'\n')
                count +=1
                print("\r当前速度:{:.2f}%".format(count*100/len(lst)),end='')
        except:
            count +=1
            print("\r当前速度:{:.2f}%".format(count*100/len(lst)),end='')
            continue
    

def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html#sh'
    stock_info_url = 'http://so.cfi.cn/so.aspx?txquery='
    output_file = 'baidustock.txt'
    slist = []
    getStockList(slist,stock_list_url)
    print(getStockInfo(slist,stock_info_url,output_file))
    

    
            

main()
