# -*- coding: utf-8 -*-
# @File  : sina_news.py
# @Author: KingJX
# @Date  : 2019/1/20 11:50
""""""
import pymysql
import requests
from lxml import etree


def get_url_page(url):
    """
    获取页面信息
    """
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def parse_page(html):
    """解析页面"""
    etree_html = etree.HTML(html)
    # 获取新闻标题
    title = etree_html.xpath('.//h1[@class="main-title"]/text()')[0]
    # 获取作者
    author = etree_html.xpath('.//p[@class="show_author"]/text()')[0]
    author = author.split('：')[1]
    # 获取时间
    time = etree_html.xpath('.//span[@class="date"]/text()')[0]
    # 获取内容
    list_content = []
    all_content = etree_html.xpath('.//div[@id="article"]/p')
    for contents in all_content:
        content = contents.xpath('./text()')[0]
        content = content.split(r'\u3000\u3000')[0].strip()
        print(content)


def main():
    # 建立数据库连接
    # db = pymysql.connect(host='localhost', user='root', password='root', database='sina_news', port=3306)
    # cursor = db.cursor()
    url = 'https://news.sina.com.cn/c/2019-01-19/doc-ihqfskcn8634011.shtml'
    html = get_url_page(url)
    parse_page(html)


if __name__ == '__main__':
    main()
