# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:26:19 2019

@author: de
"""

"""
Challenge 8
    Catch when someone submits a non integer
"""


#random number from 1 to 10

import random 

def chk_condi ():
    scrt_num = random.randint(1,10)
    usr_num=0
    
#taking numberfrom user
    try:
        usr_num =int(input("Enter the no u have gussed : ")) 
    
    except ValueError:
        print("error!!!Non- Integer")
    
    finally:
        #comparing both number
        diff=usr_num-scrt_num
        usr_attemp=0
    
    if(diff==0 + usr_attemp<5):
        print('player wins and computer lose')
        print("the secret number :{} ".format(scrt_num))
        print("number of tries left :{} ".format(5-usr_attemp))
        usr_choice()
      
        usr_attemp = usr_attemp+1   

    else:
        usr_attemp=0
        while(usr_attemp<5):
           
            diff1=usr_num-scrt_num
            
            if(diff<=5):
                print("number of tries left :{} ".format(5-usr_attemp))
                try:
                    usr_num =int(input("guess any number again :")) 
    
                except ValueError:
                    print("error!!!Non- Integer")
    
                finally:
                    
                    diff1=usr_num-scrt_num
                    usr_attemp = usr_attemp+1 
                
    
                if(diff1==0):
                    print('player wins')
                    print("the right secret number :{}".format(scrt_num))
                    break
                   

    usr_choice()
         
 
def usr_choice():   
    usr_choice1=str(input("Do you want to play again please enter 'y' for yes and 'n' for no :"))
    if (usr_choice1=='n'):
        print( "Thanks for Playing")
        exit
    elif(usr_choice1=='y'):
        chk_condi ()
    
    else :
        print("Please enter valid input : ")
        usr_choice()
        
        
chk_condi()