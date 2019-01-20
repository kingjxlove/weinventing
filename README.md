# weinventing
微银合创面试题
#### 1. [通过经纬度获取地理位置](https://github.com/kingjxlove/weinventing/blob/master/address_China.py)
        通过控制台输入经纬度, 然后调用百度地图API来获取距离该经纬度最近的城市在控制台输出, 如果不在国内,则输出在国外
        ![运行效果](https://github.com/kingjxlove/img/blob/master/%E5%9C%B0%E7%90%86%E4%BD%8D%E7%BD%AE.jpg)
#### 2. [通过URL来获取JD物品详情](https://github.com/kingjxlove/weinventing/blob/master/get_info_jd.py)
        用户可以在控制台输入JD商城的商品地址,然后可以获取到对应的物品以及物品的价格
        其实真正需要的并不是真实地址, 而是需要地址中的货物编码(也就是商品唯一ID),因为JD商城的商品价格是存储在JS中的, 并不能直接从界面中获取, 所以需要货物编码自己来构造对应的JS来获取物品的价格
        ![运行效果](https://github.com/kingjxlove/img/blob/master/JD%E5%95%86%E5%93%81.jpg)
#### 3. [爬取新浪新闻](https://github.com/kingjxlove/weinventing/blob/master/sina_news.py)
        获取新闻的标题、作者、发布时间、新闻内容.由于内用是一段段的话存储的,所以内容单独存表,通过一对多关联到新闻上.
        ![运行效果](https://github.com/kingjxlove/img/blob/master/news1.jpg)
        ![运行效果](https://github.com/kingjxlove/img/blob/master/news2.jpg)
#### 附加 [Django展示JD商品信息](https://github.com/kingjxlove/weinventing/tree/master/jd_notebook/jd_notebook)
        [通过selenium获取JD上面的笔记本信息](https://github.com/kingjxlove/weinventing/blob/master/jd_notebook/jd_notebook/others/get_info.py)
        将信息存入数据库
        ![效果](https://github.com/kingjxlove/img/blob/master/Django1.jpg)
        由于对于Vue框架不熟悉,所以没能使用Vue来展示.但是写了接口,可以通过编写接口调用后台数据
        ![效果](https://github.com/kingjxlove/img/blob/master/Django2.jpg)
        普通展示后台数据
        ![效果](https://github.com/kingjxlove/img/blob/master/Django3.jpg)
