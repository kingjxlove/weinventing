# -*- coding: utf-8 -*-
# @File  : address_China.py
# @Author: KingJX
# @Date  : 2019/1/19
""""""
import json
import urllib.request


def get_address(lat, lng):
    """
    通过经纬度获取中国的地理位置
    :param lat:纬度
    :param lng: 经度
    :return:
    """
    # 通过调用百度地图API来获取经纬度对应的省市
    url = 'http://api.map.baidu.com/geocoder/v2/?location=' + str(lat) + ',' + str(lng) + \
          '&output=json&pois=1&ak=xSoQ39HRAXfFBMEIAIv91A7txxXGmkDD'  # 构造URL
    data_address = urllib.request.urlopen(url)
    str_address = data_address.read().decode("utf-8")
    address = json.loads(str_address)


if __name__ == '__main__':
    pass
