# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 14:16:57 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format3.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    W*e*l*c*o*m*e* *t*o* *P*i*n*k* *C*i*t*y* *J*a*i*p*u*r
"""
#taking string
string=input("enter your string : ")
   
new_str="*".join(string)
print(new_str)
