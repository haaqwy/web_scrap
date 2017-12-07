#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:hzlh-wuyun 
@file: regex.py 
@time: 2017/12/07 
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen(r"http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html5lib")
images = bsObj.findAll("img", {"src": re.compile(r"../img/gifts/img.*jpg")})
for image in images:
    print(image["src"])
    print(image.attrs)
