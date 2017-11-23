#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:hzlh-wuyun 
@file: update_windows_hosts.py 
@time: 2017/11/22 
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests as rq
import os
import time

# 获取hosts内容
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'urlopen')
# html = urlopen('https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts')
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'BeautifulSoup')
# bsObj = BeautifulSoup(html.read(), 'html5lib')
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), 'hosts_content')
# hosts_content = str(bsObj.body.string)
hosts_content = rq.get('https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts').text

# 写文件hosts
with open(r'C:\Windows\System32\drivers\etc\hosts', 'w') as hosts_file:
    hosts_file.write(hosts_content)
# 刷新dns

os.system(r'ipconfig/flushdns')
