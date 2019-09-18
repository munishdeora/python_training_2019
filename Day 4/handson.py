# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:04:13 2019

@author: de
"""
# Hands On 1
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 



#using slicing concept
my_list = list ()
for n in range (1,2):
   
    my_list.append( n )
        
print("even no : " + str(my_list[1::2]))
print("odd no : "+ str(my_list[::2]))       
        
