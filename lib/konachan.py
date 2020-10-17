# -*- coding: utf-8 -*-
# @Time    : 2020-10-15
# @Author  : ohh-haolin
# @FileName: lib/konachan.py
# @Software: picSpider
# @Blog    ：https://hlz.ink


from bs4 import BeautifulSoup

from .var import *
from .utlis import *

def kDownload(url):
    html = get(url).content.decode('utf-8')

    #解析html
    soup = BeautifulSoup(html,'lxml') 
    soup = soup.find('ul',{'id':"post-list-posts"})
    
    for each_pic in soup.find_all('li',style="width: 170px;"):
        # 获得图片ID
        img_id = each_pic.get('id')[1:]
        img_orgUrl = r'https://konachan.net/post/show/{}'.format(img_id)

        # 获取图片地址
        if each_pic.find('a',class_="directlink largeimg"):
            img_url = each_pic.find('a',class_="directlink largeimg").get('href')
        elif each_pic.find('a',class_="directlink smallimg"):
            img_url = each_pic.find('a',class_="directlink smallimg").get('href')

        # 如果爬过则不爬了
        if (not checkUrlM(img_id)) or (not checkUrlPC(img_id)) :
            continue

        #log
        log(img_id, 0, 1)

        rgid = get(img_url)
        imgProcess(rgid.content, img_id, img_orgUrl)

def konachan():
    # 每日热图
    kDownload('https://konachan.net/post/popular_recent')

    # 最新的几页
    for page_num in range(1, Target[0]+1):
        #获取html
        url = 'https://konachan.net/post?page='+str(page_num)
        kDownload(url)