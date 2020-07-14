import requests
import json
import re







url1 = 'https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=9ba38dfe1da54cb6b932.1586088474.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F4630074%2F&riskLevel=1&optimusCode=10&id=4630074&userId=803983320&offset='
url2 = '&pageSize=10&sortType=1'
for n in range(1000):
    sum=0
    url = url1+'{}'.format(n*10)+url2
    params = {'uuid': '9ba38dfe1da54cb6b932.1586088474.1.0.0',
                'platform':'1',
                'partner':'126',
                'originUrl':'https://www.meituan.com/meishi/4630074/',
                'riskLevel':'1',
                'optimusCode':'10',
                'id':'4630074',
                'userId':'803983320',
                'offset':"{}".format(n*10),
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
        i['comment']
        print(i['userName']+'\u3000')
        print((i['comment']+'\n')