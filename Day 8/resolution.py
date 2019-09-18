# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:10:11 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Resolution of an Image
  Filename: 
    resolution.py
  Problem Statement:
    Find the resolution of any jpeg Image file ( width x height )
  Hint:
    https://www.programiz.com/python-programming/examples/resolution-image
"""
      
from PIL import Image
with open('b.jpg','rb') as img_file:
    width, height = Image.open(img_file).size
    print("Total resoution of image :" ,width*height)

      