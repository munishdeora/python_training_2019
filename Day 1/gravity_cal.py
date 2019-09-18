# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:03:49 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Gravity Calculator
  Filename: 
    gravity_cal.pyOutput the value meters and 
  Problem Statement:
    Compute the position of the object after falling for 10 seconds. 
    assume that the acceleration is -9.81  
    
  Hint: 
    Distance = (Acceleration*Time*Time ) / 2
"""
#time of object falling
fall_time = 10

#assume that the acceleration
acc_value=float(input("the accleration value : "))

#the position of the object after falling
print("Distance : "+str((acc_value*fall_time*fall_time ) / 2))
