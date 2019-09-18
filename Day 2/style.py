# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:54:18 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""

#taking the input from user
my_name=input("Enter your name :")


my_name_lower = my_name.lower()
print(my_name_lower)

my_name_upper = my_name.upper()
print(my_name_upper)

my_name_title = my_name.title()
print(my_name_title)



