# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:37:34 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
import csv
list1=[]
with open("romeo.txt", mode='rt') as file:
    file_contents = csv.reader(file,delimiter=' ')
    
    for item in file_contents:
        for word in item:
            list1.append(word)
            
from collections import Counter        
res=Counter(list1)        
print(res)