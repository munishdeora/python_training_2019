# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:02:22 2019

@author: de
"""

"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement: (simpsons_phone_book.txt)
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""
list1=[]
import re
with open('simpsons_phone_book.txt', mode='rt') as file :
   file_contents = file.readlines()
   
for item in file_contents :
    result= re.findall(r'^[J]+[a-zA-Z\ ]*[Neu]',item)
    if result!= []:
        list1.append(result[0])
        