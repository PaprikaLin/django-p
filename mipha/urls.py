#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/22 2:16 
# @Author : Paprika
# @File : urls.py 
# @Software: PyCharm

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index')
]