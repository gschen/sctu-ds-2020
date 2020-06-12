import requests
import json
import re
import csv

fb = open(r"C:\Users\LEGION\Desktop\meituan.csv","w",newline ='',encoding='utf-8-sig')
url1 = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=a11f57cc-9f30-48ea-844e-f2a8904f2cb7&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F162933409%2F&riskLevel=1&optimusCode=10&id=162933409&userId=&offset='
url2 = '&pageSize=10&sortType=1'
for n in range(1000):
    sum=0
    url = url1+'{}'.format(n*10)+url2
    params = {'uuid': 'a11f57cc-9f30-48ea-844e-f2a8904f2cb7',
                'platform':'1',
                'partner':'126',
                'originUrl':'https://www.meituan.com/meishi/162933409/',
                'riskLevel':'1',
                'optimusCode':'10',
                'id':'162933409',
                'userId':'184180829',
                'offset':'0',
                'pageSize':'10',
                'sortType':'1'}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'}

    r = requests.get(url,headers = headers)
    r.encoding = 'utf-8'
    s = r.text

    s = json.loads(s)
    x = s.get('data')
    y = x.get('comments')



    for i in y:
        # comment =  re.compile("'comment': '(.*?)'")
        # comments = re.findall(comment,y)
        fb.write(i['userName'],i['comment'])
        sum+=1
    # print(sum)
    # print('complete')