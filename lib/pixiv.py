# -*- coding: utf-8 -*-
# @Time    : 2020-10-15
# @Author  : ohh-haolin
# @FileName: lib/pixiv.py
# @Software: picSpider
# @Blog    ：https://hlz.ink

from .utlis import *
from .var import *
  
def pixiv():
    # 爬取前250(组)图    
    for page_num in range(1, Target[0]+1):
        # 爬取页面信息
        url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&format=json&p={}'.format(page_num)
        rsp = get(url).text
        rspJson = json.loads(rsp)

        # 遍历图片是否含有多张图片
        for content in rspJson['contents']:
            #爬取原图链接
            img_urls = content['url']
            img_urls = img_urls.replace('c/240x480/img-master','img-original')
            img_urls = img_urls.replace('0_master1200.jpg','')
            illust_page_count = int(content['illust_page_count'])
            img_id = content['illust_id']

            # 获得图片源地址
            img_orgUrl = 'https://www.pixiv.net/artworks/'+str(img_id)

            #伪造请求绕过限制
            user = {
                'Referer': img_orgUrl
            }

            # 如果爬过则不爬了
            if (not checkUrlM(img_id)) or (not checkUrlPC(img_id)) :
                continue

            #log
            log(img_id, 0, 0)
                
            # 爬取jpg格式图片
            # 为了方便维护，一个作品多张画时只保存第一张
            img_url = img_urls + '0' + '.jpg'
            rgid = get(img_url, user)

            # 有可能当前图片为png格式
            if rgid.status_code != 200:
                img_url = img_url.replace('.jpg','.png')
                rgid=get(img_url, user)

            # 存图
            imgProcess(rgid.content, img_id, img_orgUrl)