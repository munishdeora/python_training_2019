# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 12:46:50 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
file =open('absentee.txt','wt')
list1 =[]
# Taking multiple input from user
while True:
    user_input = input("Enter values ")
    
    if not user_input:
        break

    list1.append(user_input)
    
    if len(list1) == 25:
        break
for item in list1:
    file.write(str(item)+'\n') 
       
with open('absentee.txt', mode='rt') as file :
   file_contents = file.read()
   print(type(file_contents))
   print (file_contents)  
  
file.close()    
