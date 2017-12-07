#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:hzlh-wuyun 
@file: navigating_trees.py 
@time: 2017/12/07 
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(r'http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html5lib')

for child in bsObj.find('table', {'id': 'giftList'}).children:
    print(child)

print("#############################################################")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)

print("#############################################################")

print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
print(bsObj.find("img", {"src": "../img/gifts/img2.jpg"}).parent.previous_sibling.get_text())
