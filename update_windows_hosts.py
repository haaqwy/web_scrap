#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:hzlh-wuyun 
@file: update_windows_hosts.py 
@time: 2017/11/22 
"""
import requests as rq
import os

# 获取hosts内容
hosts_content = rq.get('https://raw.githubusercontent.com/googlehosts/hosts/master/hosts-files/hosts').text

# 写文件hosts
with open(r'C:\Windows\System32\drivers\etc\hosts', 'w') as hosts_file:
    hosts_file.write(hosts_content)

# 刷新dns
os.system(r'ipconfig/flushdns')
