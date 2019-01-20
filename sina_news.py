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
    news_info = {}
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
        list_content.append(content)
    news_info['title'] = title
    news_info['author'] = author
    news_info['time'] = time
    news_info['content'] = list_content
    return news_info


def db_connect(db, cursor, num, new_info):
    sql = 'insert into news(title, author, time, title_id) value ("%s", "%s", "%s", "%d")' % (new_info['title'],
                                                                                              new_info['author'],
                                                                                              new_info['time'], num)
    print(sql)
    cursor.execute(sql)
    for content in new_info['content']:
        sql = 'insert into content(content, title_id) value ("%s", "%d")' % (content, num)
        cursor.execute(sql)
        print(sql)
    db.commit()


def main():
    # 建立数据库连接
    db = pymysql.connect(host='localhost', user='root', password='root', database='sina_news', port=3306)
    cursor = db.cursor()
    urls = ['https://news.sina.com.cn/c/2019-01-19/doc-ihqfskcn8634011.shtml',
            'https://news.sina.com.cn/c/2019-01-20/doc-ihrfqziz9234102.shtml',
            'https://news.sina.com.cn/c/2019-01-19/doc-ihrfqziz9229547.shtml',
            'https://news.sina.com.cn/c/2019-01-19/doc-ihqfskcn8628004.shtml',
            'https://news.sina.com.cn/c/2019-01-19/doc-ihqfskcn8609437.shtml']
    num = 1
    for url in urls:
        html = get_url_page(url)
        news_info = parse_page(html)
        db_connect(db, cursor, num, news_info)
        num += 1


if __name__ == '__main__':
    main()
