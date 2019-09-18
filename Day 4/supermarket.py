# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:36:53 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""
dict1 = {}

while True:
    usr_ipt=input("Enter the iten name and price : ")
    if not usr_ipt:
        break
    
    
    list1=usr_ipt.split(" ")
    value = int(list1[-1])
    key = " ".join(list1[:-1])
    
    if key not in dict1:
        dict1[key] =  value
    else:
        dict1[key]=dict1[key] +value
   
print(dict1)    