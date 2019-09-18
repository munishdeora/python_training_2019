# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:11:25 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""
#Taking input string
string=input("Enter Your String : ")
str=string.replace(' ','*')
print(str)
