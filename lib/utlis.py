# -*- coding: utf-8 -*-
# @Time    : 2020-10-15
# @Author  : ohh-haolin
# @FileName: lib/utlis.py
# @Software: picSpider
# @Blog    ：https://hlz.ink

import configparser
import pymysql
import json
import datetime
import sys
import requests

from PIL import Image
from io import BytesIO

from .var import *

# 数据库
db = None
cursor = None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

# 爬虫结束后，检查url是否合法
# 调用这个语句来实现检查是
def imgProcess(data, oId, url):
    # im = Image.open('a.jpg')
    im = Image.open(BytesIO(data))
    path = r'./public/picture/{0}/{1}.webp'
    
    # pc version
    if(im.size[0] > im.size[1]):
        Index[1]+=1
        path = path.format('pc', Index[1])
        insertRecPc(Index[1], oId, url)
    # m version
    else:
        Index[0]+=1
        path = path.format('m', Index[0])
        insertRecM(Index[0], oId, url)

    # 保存
    im.save(path, "WEBP", optimize=True, quality=85, method=6)
    log(oId, 1)

# 插入前
# 检查url是否合法
def checkUrlM(id_):
    if(DB['enable'] == 'false'):
        return True

    sql = "SELECT * FROM picm WHERE originalID = {}".format(id_)
    cursor.execute(sql)
    result = cursor.fetchone()
    if(result):
        return False
    else:
        return True

def checkUrlPC(id_):
    if(DB['enable'] == 'false'):
        return True

    sql = "SELECT * FROM picpc WHERE originalID = {}".format(id_)
    cursor.execute(sql)
    result = cursor.fetchone()
    if(result):
        return False
    else:
        return True

# 插入后
# 插入记录 自增id，原始的id，链接
def insertRecM(id_, oId, url, ):
    if(DB['enable'] == 'false'):
        return

    sql = "INSERT INTO `picm` (`id`, `originalID`, `URL`) VALUES ({0}, {1}, '{2}')".format(id_, oId, url)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        db.rollback()
        return False

    # for local only
    # return True

def insertRecPc(id_, oId, url, ):
    if(DB['enable'] == 'false'):
        return

    sql = "INSERT INTO `picpc` (`id`, `originalID`, `URL`) VALUES ({0}, {1}, '{2}')".format(id_, oId, url)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        db.rollback()
        return False

    # for local only
    # return True

# 封装requests.get
def get(url, args = {}):
    hd = {}; hd.update(headers); hd.update(args)
    return requests.get(url, headers=hd, timeout=60, proxies=px)
    
# 输出的log
# id, stage, ty
def log(i, stage, ty=''):
    logStr = "{0} {1}{2}"
    # {0}
    stage = '+\t' if stage == 0 else '√\t'
    # {1}
    ty = '' if ty == '' else 'pixiv: ' if ty == 0 else 'konachan: '
    # {2}
    i = str(i)
    print(logStr.format(stage, ty, i))

# 更新数据库
def update():
    saveIndex()
    if(DB['enable'] == 'false'):
        return

    # 获取当前时间
    f = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now().strftime(f)
    # 获得上一个id
    sql = "select * from atr order by id desc limit 1"
    cursor.execute(sql)
    cId = cursor.fetchone()[0] + 1
    # 插入新时间和范围
    sql = "INSERT INTO `atr` (`id`, `lastUpdate`, `numOfMobile`, `numOfPC`) VALUES ({0}, '{1}', {2}, {3})".format(cId, now, Index[0], Index[1])
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        db.rollback()
    # 关闭database
    db.close()

# init
if(DB['enable'] == 'true'):
    db = pymysql.connect(host=DB['address'],user=DB['user'],passwd=DB['password'],db=DB['database'],port=DB['port'],charset=DB['charset'])
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    tmp = cursor.fetchone()
    if tmp:
        print('Database Connect Successful')
    else:
        print('**Warning Database Connect failed!**')
        sys.exit(1)