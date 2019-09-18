# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 14:21:12 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""
num = int(input("enter the input no : "))
i=1
for i in range(i,num+1):
    print ("*"*i)
    if (i==5):
        i=i-1
        while(True):
            print("*"*i)
            i=i-1
            if(i==0):
                break
            
    

