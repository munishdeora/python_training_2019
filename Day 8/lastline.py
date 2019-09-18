# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:23:48 2019

@author: de
"""


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
usr_ip=input("Enter file name :")
with open(usr_ip,'rt') as file:
    
    file_contents = file.readlines()
    print(file_contents[-1])