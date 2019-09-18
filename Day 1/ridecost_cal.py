# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:44:23 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
 """   
 
#per day travel
 travel_dist=int(input("enter your daily travel distance : "))
 
 #cost of Diesel
 Diesel_cost =int(input("enter the cost of desiel : "))
 
 #Fuel Average
 fuel_avg=18
 
 #cost of driving per day to office
 print("cost of driving per day to office : "+str(80*(travel_dist/fuel_avg)))
 