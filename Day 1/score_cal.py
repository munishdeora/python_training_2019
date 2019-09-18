# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 12:06:56 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""
#enter no of assignments 
ass_num=int(input("enter the number of assignment : "))

#enter no of exams 
exam_num=int(input("enter the number of exams : "))

#enter the marks in assingment
A1=int(input("enter the marks of assignment1 : "))
A2=int(input("enter the marks of assignment2 : "))
A3=int(input("enter the marks of assignment3 : "))

#enter the marks in exams
E1=int(input("enter the marks of exams : "))
E2=int(input("enter the marks of exams : "))

#weighted score

print("total weighted score :"+str(( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35))