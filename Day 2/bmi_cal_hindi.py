# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:22:56 2019

@author: de
"""

"""
Code Challenge
  Name: 
    BMI in Hindi
  Filename: 
    bmi_cal_hindi.py
  Problem Statement:
    Convert the BMI program to use hindi titles while taking input and print weight, 
    height and BMI in Hindi script using formatted strings concept   
  Hint: 
     Create a copy of the old bmi_cal.py program and do modification
"""

#assuming my weight in kilogram and height in meters
my_weight=float(input("\u0904\u0928\u091F\u0930 \u092F\u094C\u0930 \u0935\u094C \u0908\u0928 \u0915\u094C\u091C\u0940 : "))
my_height=float(input("\u0904\u0928\u091F\u0930 \u092F\u094C\u0930 \u0939\u093E\u0907\u091F \u0908\u0928 \u092E\u0940\u091F\u0930 : "))

#Calculate BMI value

bmi=((my_weight/my_height)/my_height)
print('\u092C\u0940\u0904\u092E\u093E\u0908 : {}'.format(bmi))