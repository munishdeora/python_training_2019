# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:50:22 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
list_vowel =['a','e','i','o','u','A','E','I','O','U']


state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
list1 = []

vowels = "aieouAIEOU"

for state in state_name:
    temp = ""
    for char in state:
        if char not in vowels:
            temp = temp + char
    list1.append(temp)
    

print (list1)
    

    