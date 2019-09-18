# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 16:36:25 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Adult Body Mass Index Calculator
  Filename: 
    bmi_cal.py
  Problem Statement:
    Assuming your weight in kilogram and height in meters  
    Calculate your BMI value and print it ?
  Hint: 
    Divide your weight in kilograms (kg) by your height in metres (m)
    Then divide the answer by your height again to get your BMI
"""

#assuming my weight in kilogram and height in meters
my_weight=80
my_height=1.8034

#Calculate BMI value
print((my_weight/my_height)/my_height)