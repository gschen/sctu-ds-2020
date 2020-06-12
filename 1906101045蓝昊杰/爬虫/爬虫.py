
import urllib.request
import csv
import re
import json
 
 
file = open(r"C:\Users\LEGION\Desktop\meituan.txt","w",newline ='',encoding='utf-8') 
writer = csv.writer(file)
 
class Spider:
	def loadPage(self,page):
		url = "http://cd.meituan.com/meishi/pn"+str(page)+"/"
 
		#user-Agent头
		user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0"
		headers = {"User-Agent":user_agent}
		req = urllib.request.Request(url,headers = headers)
		response = urllib.request.urlopen(req)
		html =str(response.read(),'utf8')
 
		
		#找到商家信息的内容为：{"poiId":xxx}
		#re.S 如果没有re.S,则是只匹配一行有没有符合规则的字符串，如果没有则匹配下一行重新匹配
		#如果加上re.S,则是将所有的字符串按一个整体进行匹配
		
		pattern = re.compile(r'{"poiId":.*?}',re.S)
		item_list = pattern.findall(html)#获取数据
			
		#dictinfo = json.loads(item_list[0])#把字符串转化为字典
		
		list = []#存放数据的数组
		
		for data in item_list:
				dictinfo = json.loads(data)
				writer.writerow([dictinfo["title"],dictinfo["address"],dictinfo["avgScore"],dictinfo["avgPrice"]])
		
		
 
if __name__ == "__main__":
	mySpider = Spider()
	
	for i in range(1,10):
		print("fecth:Page"+str(i))
		mySpider.loadPage(i)
		
	file.close()