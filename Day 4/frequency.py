# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:04:59 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters 
    (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
    
        
usr_str=input("enter ur input : ")
from collections import Counter        
res=Counter(usr_str)        
print(res)
        
        
        