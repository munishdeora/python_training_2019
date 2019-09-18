# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:59:08 2019

@author: de
"""


"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits 
    and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Letters 6 
    Digits 2
"""

usr_str="Python 3.2"
dict1={}
dict1['Letters']=0
dict1['Digit']=0

for item in usr_str :
    if (item.isalpha()):
        dict1['Letters']=dict1['Letters']+1
    elif(item.isdigit()):    
        dict1['Digit']=dict1['Digit']+1
        
print("Letters = ",dict1['Letters'])
print("Digit = ",dict1['Digit'])

