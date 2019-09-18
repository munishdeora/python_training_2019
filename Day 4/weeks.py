# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:24:22 2019

@author: de
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""
#tupples
weeks = ('Monday',)
w_list=list(weeks)
list1=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


for day in list1:
    if day not in w_list:
        w_list.insert(list1.index(day),day)
        
