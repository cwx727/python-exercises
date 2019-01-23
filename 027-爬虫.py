#including utf-8
import urllib.request
'''
response = urllib.request.urlopen("http://www.baidu.com") #打开网页
print(response.read())
print(response.getcode())   #返回响应吗
print(response.geturl())  #返回网址
'''

img_down = urllib.request.urlretrieve('http://www.baidu.com/img/bd_logo1.png',filename = '/home/python/ftp/share/python练习题/baidu.jpg') #下载图片


