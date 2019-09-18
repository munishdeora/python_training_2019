# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:02:24 2019

@author: de
"""

# Hands On 1  
# Make a function to find whether a year is a leap year or no, return True or False 

def leap_year (leap_year):
    if (leap_year%4==0):
        print("True")
    else:
        print("False")
   

usr_ip=int(input("Enter the year you want to check : ")) 

leap_year (usr_ip)    
        


# Hands On 2
# Make a function days_in_month to return the number of days in a specific month of a year
def days_in_month (mnth_ip):
    if(mnth_ip=="january" or mnth_ip=="march" or mnth_ip=="may" or mnth_ip=="july" or mnth_ip=="august" or mnth_ip=="octumber" or mnth_ip=="december"):
        x=31
        return x
    elif(mnth_ip=="feb"):
        x=28
        return x
    elif(mnth_ip=="april" or mnth_ip=="june" or mnth_ip=="september" or mnth_ip=="november"):
        x=30
        return x
    else:
        print("Enter valid input!!!")
    
    
mnth1_ip=input("Enter the month you want to check : ")
mnth_ip=mnth1_ip.lower()

days_in_month (mnth_ip)
  