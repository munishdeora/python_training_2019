# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:42:25 2019

@author: de
"""
"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""
list5=[]
usr_str=('')
while (True):
    ip_tuple=input("Enter values in tuple : ")
    if(ip_tuple==''):
        break
    name,a,s=ip_tuple.split(",")
    age=int(a)
    score=int(s)
    tupple=(name,age,score)
    list5.append(tupple)
        
      
print(list5.sort())  
