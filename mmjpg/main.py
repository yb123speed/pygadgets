# coding:utf-8
#!/usr/local/bin/python3

import requests
import os
import re
from bs4 import BeautifulSoup
import datetime
import time

class SpideMan(object):
    def __init__(self):
        self.urls = set()
        self.old_urls = set()
        self.old_img_urls = set() 

    def crawl(self):
        interval = 1
        date_time_mark = datetime.datetime.now()
        host = 'http://www.mmjpg.com'
        start_url=self.parser(self.download(host))
        # start_url = 'http://www.mmjpg.com/mm/1530'
        print('start_url: %s' % start_url)
        dirs = os.listdir('./Images/mm')
        old_max_mm_id = max([int(i) for i in dirs])
        # old_max_mm_id = 1525
        print('old_max_mm_id: %s' % old_max_mm_id)
        stop_url = host+'/mm/%s'%old_max_mm_id
        print('stop_url: %s'% stop_url)
        # home_page_number = `1530`
        # while True:
        #     if home_page_number == 1 :
        #         home_page_url = host
        #     else:
        #         home_page_url = host+'/home/'+home_page_number
        r_text = self.download(start_url)
        mm_page_url = self.parser(r_text)
        mm_page_content = self.download(start_url)    
        new_url_link=self.parser1(mm_page_content, start_url)
            # home_page_number=home_page_number+1
        # print new_url_link
        while not new_url_link['href'] is None and new_url_link['href'] != stop_url:
            mm_page_content = self.download(new_url_link['href'])
            new_url_link=self.parser1(mm_page_content, new_url_link['href'])
            if datetime.datetime.now() > date_time_mark + datetime.timedelta(seconds=20):
                time.sleep(2)
                date_time_mark = datetime.datetime.now()
        return

    def download(self, url):
        '''
        下载Html
        '''
        if url is None and url not in self.old_urls:
            return None
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
         like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        self.old_urls.add(url)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None

    def download_image(self, url, referer):
        '''
        下载图片
        '''
        if url in self.old_img_urls:
            return
        headers = {
            'Referer': referer,
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
         like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        ref_arr = referer.split('/')
        if len(ref_arr)==5:
            ref_arr.append('1')
        dir_url = './Images/'+ref_arr[3]+'/'+ ref_arr[4]+'/'
        print('image_url: %s' % url)
        if not os.path.exists(dir_url): 
            os.makedirs(dir_url)
        response = requests.get(url, headers=headers)
        filename = dir_url+ref_arr[5]+'.jpg'
        with open(filename, 'wb') as f:
            f.write(response.content)
            f.flush()
        print('%s downloaded.' % filename)
        self.old_img_urls.add(url)

    def parser(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = set()
        links = soup.find('a', href=re.compile(r'http://www.mmjpg.com/mm/\d+'))      
        return links['href']

    def parser1(self, html_content, referer):
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = set()
        link = soup.find('img', src=re.compile(r'http://fm.shiyunjj.com/\d+/\d+/\w+.jpg'))      
        self.download_image(link['src'], referer)
        link1 =soup.find('a', href=re.compile(r'http://www.mmjpg.com/mm/\d+'))
        return link1


if __name__ == "__main__":
    spide_man =SpideMan()
    spide_man.crawl()
