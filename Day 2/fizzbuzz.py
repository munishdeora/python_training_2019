# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:00:19 2019

@author: de
"""

"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""
n=1
while(n<=100):
    if(n%3==0 and n%5==0):
        print("FizzBuzz")
        n=n+1
    elif(n%3==0):
        print("Fizz")
        n=n+1
    elif(n%5==0):
        print("Buzz")
        n=n+1

    else:
        print(n)
        n=n+1
        
    
