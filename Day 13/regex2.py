# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:48:30 2019

@author: de
Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""
N=[]
List1=[]
while(True):
    usr_ip=input("enter the values : ")
    if not usr_ip :
        break
    N.append(usr_ip)
    
import re

N = ["lara@hackerrank.com","brian-23@hackerrank.com","britts_54@hackerrank.com"]

for item in N:
    result= re.match(r'^[a-zA-Z\d\-\_]+\@[a-zA-Z\d]+\.[a-zA-Z]{2,4}$',item)
    if result == None :
        pass
    else:
        List1.append(item)
List1.sort()        
print(List1)        