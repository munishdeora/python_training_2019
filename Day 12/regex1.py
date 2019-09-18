# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:13:19 2019

@author: de

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
N=[]
List1=[]
while(True):
    usr_ip=input("enter the values : ")
    if not usr_ip :
        break
    N.append(usr_ip)
    
import re
for item in N:
    result= re.match(r'^[\+\-\.0-9\n]+\.',item)
    if result == None :
        print('False:')
    else:
        print('True :')