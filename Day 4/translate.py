# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:59:00 2019

@author: de
"""


"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

def translate(list1):
    for char in list1:
        if char not in vowel:
            char=char+"o"+char
            list2.append(char)
        else:
            list2.append(char)
    
    print("".join(list2))


vowel="aeiouAEIOU "
list2=[]

usr_ip=input("Enter your text you want to convert : ")
list1=list(usr_ip)
translate(list1)
