# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:40:45 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format4.py
  Problem Statement:
    This program accepts the user's first name and last name 
    Print them in reverse order with a space between them.
    Take Input from User 
    Your code should have only a single user input statement.  
  Hint:
    Try to serach for some function in the str using help() and dir()
  Input:
    Forsk Technologies
  Output:
    Technologies Forsk
"""
#accepts the user's first name and last name
string=input("Enter your first name and last name : ")
index=string.find(" ")
print(string[index+1:]+" "+string[0:index])

