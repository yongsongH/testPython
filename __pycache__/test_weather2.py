'''
Created on 2016-5-11

@author: hys mac
'''
#coding：utf8
import urllib.request
import urllib.parse
import json
"""
    利用“中国天气网”抓取桂林天气情况
    http://www.weather.com.cn/weather1d/101300501.shtml#input
 
"""

class ChinaWeather(object):
    def __init__(self):
        self.url = 'http://www.weather.com.cn/weather1d/101300501.shtml#input'
        self.headers = {}
        self.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        self.data = {}
        self.city = '桂林'
    
    
    def spider(self):
        data = urllib.parse.urlencode({'cityCode':self.cities[self.city]}).encode('utf-8')
        req = urllib.request.Request(self.url,data,self.headers)
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        
    def json_parse(self,html):
        target = json.loads(html)
        high_temp = target['data'][0]['actual']['high']
        low_temp = target['data'][0]['actual']['low']
        current_temp = target['data'][0]['actual']['tmp']
        today_wea = target['data'][0]['actual']['wea']
        air_desc = target['data'][0]['actual']['desc']
        print('%s: %s~%s°C 现在温度 %s°C 湿度：%s %s'%(self.city,high_temp,low_temp,current_temp,today_wea,air_desc))
    
    



if __name__ == '__main__':
    weather_spider = ChinaWeather()
    weather_spider.spider('桂林')