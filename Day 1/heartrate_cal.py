# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 17:04:21 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Target Heart Rate Calculator
  Filename: 
    heartrate_cal.py
  Problem Statement:
    Calculate the Maximum Heart Rate and Target Heart Rate Range 
    ( Lower and Higher value ) of a person of a specific age.
    Lets Assume your age is 21 years
  Hint: 
    Subtract your age from 220 to get your Maximum Heart Rate
    Lower end of your Target Heart Rate is 70% of Maximum Heart Rate
    Higher end of your Target Heart Rate is 85% of Maximum Heart Rate
    Heart Rate = Beats per minute 
"""


#Assume your age is 21 years
my_age=int(input("enter your age: "))

#your Maximum Heart Rate
max_heart= (220-my_age)
print("maximum your heart rate : "+str(max_heart))

#Lower end of your Target Heart Rate
maximum_heartrate =((max_heart*70)/100)
print("Lower end heart rate : "+str(maximum_heartrate))

#Higher end of your Target Heart Rate
minimum_heartrate =((max_heart*85)/100)
print("heigher end heart rate : "+str(minimum_heartrate))
