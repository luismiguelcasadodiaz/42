# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 07:53:15 2023

@author: luism
"""
import requests
import urllib

import re

def no_recursive(url, path):
  print(f"-{url}-")
  html = urllib.request.urlopen(url).read().decode('utf-8')
  print(html)
  
  pat_img =r'<img alt=\"(.*)\" data-full'      #El Mundo
  #pat_img =r'<img src=\"(\S*)\"'      #EL debate
  images = re.findall(pat_img, html, re.MULTILINE)
  for image in images:
    print(image)
  
  
def recursive(url, path, level):
  print("No recursive", url, path, level)
  
  
no_recursive('https://www.elpais.com/','data')