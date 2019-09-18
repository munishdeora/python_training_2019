# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:52:28 2019

@author: de
"""


"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is the 
    mean average of the values, except ignoring the largest and smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. Use int division to produce the final average. 
    You may assume that the array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""
usr_ip=input("Enter the input : ")
list1=usr_ip.split(',')
listf=[]

for char in list1:
    x=int(char)
    listf.append(x)

#
list2=[]
for char in listf:
    if char not in list2:
        x=int(char)
        list2.append(x)
list2.sort()    
 
list2.pop()
del  list2[0]   
le=len(list2)
x=0
for item in list2:
    x=x+item
    
avg=x/le   
print(int(avg))