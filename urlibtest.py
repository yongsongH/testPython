'''
Created on 2016-4-13

@author: hys mac
'''
#coding:utf8
import urllib.request
from http import cookiejar
#import html.parser
#import cookielib
url ="http://www.baidu.com"
print ('第一种方法')
response1=urllib.request.urlopen(url)
print (len(response1.read()),)
print (response1.getcode(),)
print ( )
print ('第二种方法')
request=urllib.request.Request(url)
request.add_header("use-agent", "mozilla/5.0")
response2=urllib.request.urlopen(url)
print (len(response2.read()),)
print (response2.getcode(),)
print ( )
#print ('第三种方法')
#cj = cookiejar.CookieJar()
#opener = urllib.request.bulid_opener(urllib.request.HTTPCookieProcessor(cj))
#urllib.request.install_opener(opener)
#response3=urllib.request.urlopen(url)
#print (len(response3.read()),)
#print (response3.getcode(),)
#print ( )
print('第三种方法')
cj =cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(response3.read())
#print (len(response3.read()),)