# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:06:55 2019

@author: de
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
      import random

    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print (names)

As you can see, this algorithm can potentially assign the same secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.

"""
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
my_list=[]
import random

for i in range(len(names)):
    names[i] = random.choice(code_names)
print (names)
    
my_list=list(map(lambda x: random.choice(code_names) , names))  

num=0
while(num < 20):
    
    num=num+1
    if num == 8:
        continue
    print(num)