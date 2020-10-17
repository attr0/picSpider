# PixSpider

## Summary

基于Python和PHP的爬爬怪服务，图片爬自于Pixiv和Konachan。

本项目特点：

1. 整合了爬虫和随机图片，同时可以通过修改配置文件单独工作。
2. 利用数据库，避免重复爬图的情况，同时实现了些许API
3. 区分手机版和电脑版本图片，同时通过Webp格式存储图片



## Demo

### 图片

![Miku!](https://ohh-haolin.github.io/picSpider/public/picture/pc/0.webp)

### 查询页面

[GitHub](https://ohh-haolin.github.io/picSpider/public/)（无后端，仅能预览前端）



## Requirements

仅本地：

- Python > 3.6 with 
  - Requests
  - Pillow
  - bs4
  - pymysql
  - configparser
  - lxml
  

配合查询页面和防重复：

- PHP > 7.0
- Mysql > 5.1



## Install

1. 编辑`conf.ini`， 其中

   - ID区表示文件保存的起始ID（每次爬完图片后会自动更新）
   - Target区表示要爬的页数
   - DB区表示数据库配置
   - Proxy区表示代理配置

   当DB区的`enable = false`时会使用本地模式

   

2. 数据库配置

   如果只想用本地模式可以略过

   把`setup/picSpider.sql`恢复到某个数据库中，并修改`conf.ini`文件



3. 网页配置

   修改网站目录为根目录，修改运行目录为`public`

   


3. 运行即可

   自行修改pathToFolder

   ```bash
   cd pathToFolder
   python -u picSpider.py #或 python3 ...
   ```


