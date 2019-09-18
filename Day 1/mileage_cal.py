# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:37:22 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Gas Mileage Calculator
  Filename: 
    mileage_cal.py
  Problem Statement:
    Assume my car travels 100 Kilometres after putting 5 litres of fuel. 
    Calculate the average of my car. 
  Hint: 
    Divide kilmeters by the litres used to get the average
"""

#car travels
car_km=int(input("enter your car run in kilometers : "))

#putting x litres of fuel
my_fule=int(input("enter fules in liters : "))

#average of my car
print("average of car : "+str(car_km/my_fule))