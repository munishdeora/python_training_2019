# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:35:57 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title        Author      Quantity  Price per Item
    34587         Learning Python,  Mark Lutz   4         40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, 
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""
order=[[34587,'Learning Pyth','Mark Lutz',4,40.95],
       [98762,'Programming Python','Mark Lutz',5,56.80],
       [77226,'Head First Python','Paul Barry', 3 ,32.95],
       [88112,'Einführung in Python3','Bernd Klein',3,24.99]]

item_order=[]
invoice_order=[]
min_order=100

item_order = list(map(lambda x : (x[0] , round( x[3] * x[4] ,2)), order))

invoice_order = list(map(lambda x :x if x[1]>=min_order  else (x[0],x[1]+10) ,item_order))

print(invoice_order)

"""

list1=[[34587,'Learning Pyth','Mark Lutz',4,40.95],
       [98762,'Programming Python','Mark Lutz',5,56.80],
       [77226,'Head First Python','Paul Barry', 3 ,32.95],
       [88112,'Einführung in Python3','Bernd Klein',3,24.99]]


listf=[]
list_final=[]
list_temp=[]
listp=[]

from functools import reduce 
for i in range (0,4):  
   list_temp.append(reduce(lambda x,y: float(list1[i][3])*list1[i][4] ,list1) ) 
    
   
for i in range (0,4):    
    listf.append(list1[i][0])
    

######listp.append(reduce(lambda x : 100 if x<100 : x+10 ,list_temp) )
        
for i in range (0,4):  
    if (list_temp[i]<100):
        list_temp[i]=list_temp[i]+10
  
list_final=[[tuple(listf),tuple(list_temp)]]
"""

    