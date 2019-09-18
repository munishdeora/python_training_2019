# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 13:46:22 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values with original 
    order reserved  
  Hint: 
    Distance = (Acceleration*Time*Time ) / 2
"""

list1=[12,24,35,24,88,120,155,88,120,155]
my_list=list(dict.fromkeys(list1))

print(my_list)
