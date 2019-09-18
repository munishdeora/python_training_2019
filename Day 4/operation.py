# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:40:58 2019

@author: de


Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""

def Add1(listf):
    print ("Sum =",functools.reduce(lambda x,y: x+y, listf))

def Multiply(listf):
    print ("Multiply =",functools.reduce(lambda x,y: x*y, listf))

def Largest(listf):
    listf.sort()
    print("Largest = ",listf[-1])
    
def Smallest(listf):
    listf.sort()
    print("Smallest = ",listf[0])  

def Sorted(listf):
    listf.sort()
    print("Sorted = ",listf) 

def Without_Duplicates (listf):
    list2=[]
    for char in listf:
        if char not in list2:
            x=int(char)
            list2.append(x)
    print("Without_Duplicates = ",list2)       
            
            
       
    
   
def my_function(listf):
    Add1(listf)
    Multiply(listf)
    Largest(listf)
    Smallest(listf)
    Sorted(listf)
    Without_Duplicates (listf)
   
    
usr_ip=input("Enter the list of numbers for operation : ")
list1=usr_ip.split(',')
listf=[]
for char in list1:
    x=int(char)
    listf.append(x)
    

import functools
my_function(listf) 
    
    