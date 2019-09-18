# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:51:17 2019

@author: de



Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
    
    
"""   

def reverse(ip_str):
    xyz=ip_str[::-1]
    print(xyz)
    
    


ip_str=input("Enter your input : ")    

reverse(ip_str)
