# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:32:54 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv
dict1={}
dict1['elephant']=0
dict1['tiger']=0
dict1['lion']=0
dict1['zebra']=0
dict1['kangaroo']=0

with open("zoo.csv", mode='rt') as file:
    file_contents = csv.reader(file,delimiter=',')

   
    for item in file_contents:
        
        if (item[0]=='elephant'):
            dict1['elephant']=dict1['elephant']+int(item[2])
            
        if (item[0]=='tiger'):
            dict1['tiger']=dict1['tiger']+int(item[2])
            
        if (item[0]=='lion'):
            dict1['lion']=dict1['lion']+int(item[2])
            
        if (item[0]=='zebra'):
            dict1['zebra']=dict1['zebra']+int(item[2])
            
        if (item[0]=='kangaroo'):
            dict1['kangaroo']=dict1['kangaroo']+int(item[2])
        
print(dict1)        
print("Total : ",sum(dict1.values()))        
        
        