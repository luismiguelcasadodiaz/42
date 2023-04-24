# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 07:53:15 2023

@author: luism
"""
import requests
import urllib

import re

def find_images_in_url(url):
  print(f"searching images -{url}-")

def find_links_in_url(url):
  print(f"searching links -{url}-")

def img_scrapper(url, path: str, recursive: bool, level=5):
  """
  Parameters:
    url: the url to start scrap from
    path : a path for saving url images
    recursive: boolean, indicates if recursively scrap links founds
    level : int . set the deep for recur

  Returns
    a dictionary whose key is an url os an image
  """
  print(f"at level {level} scrapping -{url}-")
  image_urls = {}
  if not recursive:
    image_urls = find_images_in_url(url)
    return image_urls
  elif level > 0:
    image_urls = find_images_in_url(url)
    links_url = find_links_in_url(url)
    not_visited_links = filter_links(url)
    for link in not_visited_links:
      this_link_images = img_scrapper(link, path, recursive, level - 1)
      image_urls.update(this_link_images)
    return image_urls

    
  pat_img =r'<img alt=\"(.*)\" data-full'      #El Mundo
  #pat_img =r'<img src=\"(\S*)\"'      #EL debate
  images = re.findall(pat_img, html, re.MULTILINE)
  for image in images:
    print(image)
  
