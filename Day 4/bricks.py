# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:29:33 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""
usr_ip=input("Enter the number of small bricks,big bricks and target row :  ")
list1=usr_ip.split(" ")
small_brick = int(list1[0])
big_brick = 5*int(list1[1])
trg_inch=int(list1[2])


if (small_brick+big_brick>=trg_inch):
    print("True")
else:
    print("False")    