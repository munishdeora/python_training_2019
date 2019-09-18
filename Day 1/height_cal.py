# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:17:18 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Height Calculator
  Filename: 
    height_cal.py
  Problem Statement:
    Lets assume your height is 5 Foot and 11 inches 
    Convert 5 Foot into meters and 
    Convert 11 inch into meters and 
    print your total height in meters and 
    print your total heigjt in centimetres also 
  Hint: 
    1 Foot = 0.3048 meters 
    1 inch = 0.0254 meters 
    1 m = 100 cm 
"""

#assuming my age
my_height = input("Enter your Height: ")
h1,h2 = my_height.split(".")


#one foot and inch in meters
one_foot=0.3048
one_inch=0.0254

one_foot*int(h1)
#total height in meter
print("your total height in meters = "+str(one_foot*int(h1)+one_inch*int(h2)))


#total height in centimeter
print("your total height in centimeter = "+str(100*(one_foot*5+one_inch*11)))