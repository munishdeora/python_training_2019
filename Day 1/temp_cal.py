# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:21:18 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Temperature Calculator
  Filename: 
    temp_cal.py
  Problem Statement:
    Assume today's temperature in Jaipur is 29 degree Centigrade. 
    Calculate the temperate in Degree Fahrenheit and print it.
    Calculate the temperature in Degree Kelvin and print it.
  Hint: 
    Multiply by 9/5 and add 32  to get in Fahrenheit
    Add 273 approximately to get in Kelvin
"""
#today's temperature
tod_temp=int(input("enter today's temperature : "))

#temperate in Degree Fahrenheit
print("temperate in Degree Fahrenheit :"+str(32+(tod_temp*1.8)))

#temperature in Degree Kelvin
print("temperature in Degree Kelvin : "+str(tod_temp+273))
