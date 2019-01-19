# -*- coding: utf-8 -*-
# @File  : get_info_jd.py
# @Author: KingJX
# @Date  : 2019/1/19
""""""
import requests
import json
import xlwt
from lxml import etree


def get_url_page(url):
    """
    获取页面信息
    :param url: 传入页面地址
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('GBK')
        return text
    return None


def parse_page(html):
    pass


def main():
    url = 'https://item.jd.com/7765111.html'
    html = get_url_page(url)
    print(html)


if __name__ == '__main__':
    main()
