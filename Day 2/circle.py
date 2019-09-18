# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:39:08 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Area and Perimeter of Circle
  Filename: 
    circle.py
  Problem Statement:
    Take the radius of the circle from the keyboard as input from the user 
    Calculate the area and perimeter of it.
  Hint: 
    Pi * radius * radius is the area of circle
    2 * Pi * radius is the perimeter of circle 
    Use math module to get the value of Pi ( 3.14 ) 
  Input:
    Take the radius from the keyboard as input from the user.
"""
#Take the radius of the circle
radius_cir=int(input("Enter the radius of the circle : "))
from math import pi

#area of circle
print("area of circle : "+str(pi*radius_cir*radius_cir))

#peremeter of circle
print("perimeter of circle : "+str(2*pi*radius_cir))