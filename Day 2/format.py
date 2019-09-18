# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:05:03 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format.py
  Problem Statement:
    This program prints out the following string in a specific format (see the output). 
  Hint: 
    The string should be printed using a single print statement only and 
    the indexes shouldn't be counted manually.
  Input:

    This is a multi line string. This code challenge is to
    test your understanding about strings.
    You need to print some part of this string.
    From here print this text without manually counting the indexes.
  Output:
    From here print this text without manually counting the indexes.
"""
string=input("Enter your string : ")

index=string.find("From")
print(string[index:])