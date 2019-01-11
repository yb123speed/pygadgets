# _*_ coding:utf-8 _*_
import requests
from lxml import etree

class VideoSpider(object):

    def start_request(self):
        for i in range(1, 224):
            print("==========正在抓取第%s页==========" % i)
            response = requests.get("https://ibaotu.com/shipin/7-0-0-0-0-"+str(i)+".html")
            html = etree.HTML(response.content.decode())
            self.xpath_data(html)

    def xpath_data(self,html):
        pass