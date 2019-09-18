# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 16:02:57 2019

@author: de
"""

# Hands On  1
# Print all the numbers from 1 to 10 using condition in while loop
n=1
while (n<=10):
    print (n)
    n = n +1

# Hands On  2
#  Print all the numbers from 1 to 10 using while True loop
n = 1
while(True):
    print(n)
    n=n+1
    if(n==11):
        break

# Hands On 3
#  Print all the even numbers from 1 to 10 using condition in while loop
n=1
while(n<=10):
    if(n%2==0):
        print(n)
        n=n+1 
    else:
        n=n+1    
        
    
# Hands On 4
#  Print all the even numbers from 1 to 10 using while True loop  
n=1
while(True):
    if(n%2==0):
        print(n)
        n=n+1
    else:
        n=n+1
    
    if(n==11):
        break

# Hands On 5
#  Print all the odd numbers from 1 to 10 using condition in while loop
n = 1
while(n<=10):
    if(n%2!=0):
        print(n)
        n=n+1
    else:
        n=n+1
        
# Hands On 6
#  Print all the odd numbers from 1 to 10 using while True loop
n=1
while(True):
    if(n%2!=0):
        print(n)
        n=n+1
    else:
        n=n+1
        
    if(n==11):
        break
    
# Hands On 7
#  Print all the prime numbers from 1 to 10 using condition in while loop
n = 1
while(n<=10):
    if(n//n==1):
        print(n)
        n=n+1
    else:
        n=n+1
        
        
    
  
    