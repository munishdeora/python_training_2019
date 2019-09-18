# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:03:12 2019

@author: de
"""
"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
    Then ask you ( Player ) to guess the number and store as guess number

    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

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
    print("player lose and computer wins")    
    
print(Comp_random)


