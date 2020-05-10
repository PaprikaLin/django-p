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
    path('p/<int:page_num>', views.post_view, name='post'),
    path('m/p/<int:page_num>', views.post_view, name='m_post'),
    path('page/<str:page>', views.page_view, name='page'),
    #path('', views.IndexView.as_view(), name='index'),
    path('form/', views.comment_form, name='comment_form'),
    path('m/', views.mobile_index, name='mobile_index'),
    path('api/comment', views.increase_like_or_unlike, name='increase_like_or_unlike'),
    path('m/api/comment', views.increase_like_or_unlike, name='increase_like_or_unlike'),
    path('updates/', views.updates_page, name='updates_page'),
    path('upload/', views.upload, name='upload'),
    path('api/upload/', views.api_upload, name='api_upload'),
    path('m/upload/', views.upload, name='m_upload'),
    path('api/newcomment', views.new_comment, name='new_comment'),
    path('api/getcomment/<int:post_id>', views.get_comment, name='get_comment'),
    path('magicrealism/', views.magic_realism, name='magic_realism'),
    path('positiveenergy', views.positive_energy, name='positive_energy')
    # 定义访问不同的地址返回不同的模板，
    #path('<str:author>/', views.AuthorPoetsView.as_view(), name='author_poets'),
    # re_path(r'^author/(\w+)$', views.author_poets, name='author_poets')
    #path('<str:author>/<int:slug>/', views.PoetView.as_view(), name='poet_page'),
    # 测试表单
]