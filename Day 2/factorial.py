# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:21:32 2019

@author: de
"""



"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""
#taking i/p from user
fact_numb=int(input("Enter the number for which you have to find out the factorial : "))

#using dir and help
import math
dir (math)
help(math.factorial)

#Facorial of given no
math.factorial(fact_numb)