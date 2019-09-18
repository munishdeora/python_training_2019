# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:11:48 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""
ip_str=input("Entr a string you want to check PANGRAM or not : ")
ip_str2=ip_str.lower()
alp=("abcdefghijklmnopqurstuvwxyz")
list1=list(ip_str2)
list2=list(alp)
listc=[]

c=0
for char in list2:
    if char not in list1:
        
        listc.append("NOT PANGRAM")
        c=0
    else:
        listc.append("PANGRAM")
        c=c+1

if(c==len(listc)):
    print("PANGRAM")
else:  
    print("non panagram")