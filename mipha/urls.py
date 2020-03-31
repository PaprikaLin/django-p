#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/12/22 2:16 
# @Author : Paprika
# @File : urls.py 
# @Software: PyCharm

from django.urls import path, re_path

from . import views

app_name = 'mipha'
urlpatterns = [
    path('', views.index, name='index'),
    #path('post/<int:year>/<int:month>/<int:day>/<str:title>/', views.post_view, name='post'),
    path('p/<int:id>', views.post_view, name='post'),
    path('page/<str:page>', views.page_view, name='page'),
    #path('', views.IndexView.as_view(), name='index'),
    path('form/', views.comment_form, name='comment_form'),
    # 定义访问不同的地址返回不同的模板，
    #path('<str:author>/', views.AuthorPoetsView.as_view(), name='author_poets'),
    # re_path(r'^author/(\w+)$', views.author_poets, name='author_poets')
    #path('<str:author>/<int:slug>/', views.PoetView.as_view(), name='poet_page'),
    # 测试表单
]