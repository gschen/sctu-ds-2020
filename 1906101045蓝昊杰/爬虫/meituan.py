import json
import requests
import xlwt


workbook = xlwt.Workbook(encoding='utf-8')

worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0, 0, label='店名：卡麦斯烘培')
worksheet.write(0, 1, label='地址：青羊区罗家碾街43号附16号（文汇苑旁）')
worksheet.write(0, 2, label='电话：13540852569')
worksheet.write(0, 3, label='营业时间：周一至周日 08:00-22:00')
worksheet.write(1, 0, label='用户名')
worksheet.write(1, 1, label='评价')
worksheet.write(1, 2, label='评论')
m=2
n=0
for i in range(10):
    url ='https://www.meituan.com/meishi/api/poi/getMerchantComment?uuid=d2a718e8dc604835823e.1591866621.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fwww.meituan.com%2Fmeishi%2F4586632%2F&riskLevel=1&optimusCode=10&id=4586632&userId=&offset='+'{}'.format(i*10)+'&pageSize=10&sortType=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Cookie': '_lxsdk_cuid=16fd1466346c8-0a4eec556b28c7-7711a3e-144000-16fd1466346c8; _hc.v=524bdcb0-6f62-3ccb-43dd-7e1ddfad7889.1579764982; _ga=GA1.2.592801623.1579764064; client-id=7ef44bd8-dd5b-4424-8ed8-8cf54041a51d; mtcdn=K; lsu=; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1591857978; __utma=211559370.592801623.1579764064.1581665500.1591857978.3; __utmz=211559370.1591857978.3.3.utmcsr=baidu|utmccn=baidu|utmcmd=organic|utmcct=zt_search; __mta=156139140.1579764057753.1579764057753.1591857986632.2; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=16fd1466346c8-0a4eec556b28c7-7711a3e-144000-16fd1466346c8; ci=59; rvct=59%2C1167; uuid=d2a718e8dc604835823e.1591866621.1.0.0; lat=30.672937; lng=104.025729; _lxsdk_s=172a6f89565-ef5-b16-161%7C%7C11'
      }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text

    html=json.loads(html)




    datas = html.get('data')

    items_list=datas.get('comments')




    for j in items_list:
        worksheet.write(m, n, label=str(j["userName"]))
        worksheet.write(m, n+1, label=str(int(j['star'])//10)+'星')
        worksheet.write(m, n+2, label=str(j["comment"]))
        m+=1
        n=0


workbook.save('Excel_test.xls')

