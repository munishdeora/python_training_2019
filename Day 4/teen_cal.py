# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:36:08 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
    
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""
dict1={"a" : 2, "b" : 15, "c" : 13}


def fix_teen(n):
    if n in (13,14,17,18,19):
        return 0
    else:

        return n



res=map(fix_teen ,dict1.values() )
print("Sum = " ,sum(list(res)))

           
