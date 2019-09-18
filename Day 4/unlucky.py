# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:49:07 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""


usr_ip=input("Enter the input : ")
list1=usr_ip.split(',')
listf=[]
list1 = list(map(int, list1))



for index, item in enumerate(list1):
    if item == 13:
        listf.append(index)
        if index != len(list1)-1:
            listf.append(index+1)


some = 0

for index, item in enumerate(list1):
    if index not in listf:
        some = some + item
        
    
    