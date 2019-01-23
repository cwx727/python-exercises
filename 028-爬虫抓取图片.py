#including utf-8
import urllib.request
import re
import time

def getHtml(url):
	response = urllib.request.urlopen(url)
	response_ret = response.read()
	return response_ret.decode('utf-8')    #把返回转换成utf-8格式
	
def getImg(response):
	imgList = re.compile(r'src="(https.*?\.(jpg|png))"').findall(response)
	
	print(imgList)

	x=0
	for imgurl in imgList:
		urllib.request.urlretrieve(imgurl[0],'./028-爬虫抓取图片img/%d.png'%x)
		x+=1
		time.sleep(1)

	
response =getHtml("https://blog.csdn.net/")

getImg(response)
