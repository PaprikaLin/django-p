#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/4/9 14:44 
# @Author : Paprika
# @File : test.py 
# @Software: PyCharm

import requests


def r(file):
    url = 'https://pic.suo.dog/api/tc.php?type=1688&echo=imgurl'

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://pic.suo.dog/'
    }

    res = requests.post(url, headers=headers, files=file)
    return res.text

