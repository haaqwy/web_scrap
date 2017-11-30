#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:hzlh-wuyun 
@file: war_and_peace.py 
@time: 2017/11/29 
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen(r'http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html, 'html5lib')
name_list = bsObj.findAll('span', {'class': 'green'})
for name in name_list:
    print(name.get_text())
