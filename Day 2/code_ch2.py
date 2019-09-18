# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:19:27 2019

@author: de
"""

"""
Challenge 2
    Print the secret number and guess number when Player loses using format function 
"""
#random number from 1 to 10

import random 
Comp_random = random.randint(0,10)


#taking numberfrom user
usr_num = int(input("Enter the number you have guess :"))

#comparing both number
if(usr_num==Comp_random):
    print('player wins and computer lose')
    
else:
    print("the secret number :{} and user guessed number :{}".format(Comp_random,usr_num))    
    
