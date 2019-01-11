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
        src_list = html.xpath('//div[@class="video-play"]/video/@src')
        tit_list = html.xpath('//span[@class="video-title"]/text()')
        for src, tit in zip(src_list, tit_list):
            url = "http:" + src
            file_name = tit + ".mp4"
            response = requests.get(url)
            print("正在抓取文件：" + file_name)
            with open(file_name, "wb") as f:
                f.write(response.content)

if __name__ == "__main__":
    spider = VideoSpider()
    spider.start_request()