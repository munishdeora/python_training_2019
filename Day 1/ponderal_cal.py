# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:55:04 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Ponderal Index Calculator
  Filename: 
    ponderal_cal.py
  Problem Statement:
    Calculate the Ponderal Index of a Person and print it
  Hint: 
    Divide the BMI by your Height ( meters ) to get your Ponderal Index
"""

#assuming my weight in kilogram and height in meters
my_weight=80
my_height=1.8034

#Calculate Ponderal Index value
print(((my_weight/my_height)/my_height)/my_height)

