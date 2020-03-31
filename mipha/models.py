#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/22 2:16 
# @Author : Paprika
# @File : urls.py 
# @Software: PyChar
from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


# 文章模型
# 注意如果有数据之后就比较难再更改
# 要么新添加的字段要有default数据，要么统一设置为null
class Post(models.Model):
    title = models.CharField(max_length=200)
    #author = models.CharField(max_length=200)
    #slug = models.CharField(max_length=200) # 文章网址
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    mail = models.EmailField(blank=True)
    visible = models.BooleanField(default=True)
    ip_addr = models.TextField()

    # class Meta 内的设置则要指定文章显示的顺序是以pub_date为依据
    class Meta:
        ordering = ('-pub_date', )

    # 作用跟__str__一样，在cmd界面显示标题，用unicode是因为可以正确显示中文
    # 还是需要 __str__ 才能正常显示
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
