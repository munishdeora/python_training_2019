# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:36:55 2019

@author: de
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
usr_ip=input("Enter the input : ")
list1=usr_ip.split(',')
tuple1=tuple(list1)
