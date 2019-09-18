# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:05:42 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Different sizes
  Filename: 
    png.py
  Problem Statement:
    Convert all files PNG in a directory into different sizes
  Hint: 
    os.listdir('.') function will list all the files in the current directory   
"""
import os
from PIL import Image
for file_name in os.listdir("."):
    try:
        name,ext=file_name.split(".")
        if (ext=="jpg"):
            file_name = Image.open(file_name)
            file_name.save('{}.png'.format(name))
        else:
            pass
    except Exception:
           print("hell!!!")
        
