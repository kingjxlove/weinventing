
from django.db import models


class Notebook(models.Model):
    # 货物ID
    g_id = models.IntegerField(unique=True, blank=True, null=True)
    # 名称
    name = models.CharField(max_length=255, blank=True, null=True)
    # 店铺
    shop = models.CharField(max_length=255, blank=True, null=True)
    # 价格
    price = models.FloatField(blank=True, null=True)
    # 图片地址
    img = models.CharField(max_length=255, blank=True, null=True)
    # 评论数量
    commit_num = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'notebook'
