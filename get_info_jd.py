# -*- coding: utf-8 -*-
# @File  : get_info_jd.py
# @Author: KingJX
# @Date  : 2019/1/19
""""""
import requests
import json
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


def parse_page():
    url = 'https://item.jd.com/3290987.html'
    html = get_url_page(url)
    print(html)
    etree_html = etree.HTML(html)
    info = {}
    # 获取好评率
    comm = etree_html.xpath('.//div[@class="percent-con"]')
    return comm


def get_name_price(url_1):
    # 构造价格数据URL
    num = url_1.split('/')[-1].split('.')[0]
    url = 'https://c.3.cn/recommend?callback=handleComboCallback&methods=accessories&p=103003&sku=%s' % num
    url += '&cat=670%2C671%2C672&lid=1&uuid=572822970&pin=&ck=pin%2CipLocation%2Catw%2Caview&lim=5&cuuid=572822970&csid=122270672.7.572822970%7C27.1547907196&_=1547910477315'
    html = get_url_page(url)
    goods_info = html.split('handleComboCallback(')[1][:-1]
    json_goods = json.loads(goods_info)
    # 获取商品名称
    name = json_goods['accessories']['data']['wName']
    # 获取商品价格
    price = json_goods['accessories']['data']['wMaprice']
    dict_info = {}
    dict_info['name'] = name
    dict_info['price'] = price
    return dict_info


def main():
    url = input('请输入要解析的商品地址:')
    goods_info = get_name_price(url)
    print("商品名称为:", goods_info['name'])
    print('商品价格为:', goods_info['price'])


if __name__ == '__main__':
    main()
