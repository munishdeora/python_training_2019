    # -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:44:03 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
  Input: 
    12 9 61 5 14
  Output:
    True
"""
usr_ipt=input("enter the no : ")
list1=usr_ipt.split(" ")
len1=len(list1)
listc=[]
for item in list1: 
    n=list1.index(item)
    if (item==list1[len1-1]):
        
        listc.append("true")
        
        len1=len1-1
        
    else:
        listc.append("false")
        len1=len1-1
c=0
for check in listc:
    if (check=="true"):
        c=c+1
    else:
        c=0
        
        
if (c==len(list1)):
    print("true")
else:
    print("false")    
    