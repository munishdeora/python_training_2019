# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:04:10 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Unicode Printing
  Filename: 
    unicode_print.py
  Problem Statement:
    Print the below string as it is   
    UNIX® and Sun Microsystem™ are Copyright ©, 2019 Oracle
  Hint: 
    Use unicode \u00AE for Registered ® 
    Use unicode \u00A9 for Copyright © 
    Use unicode \u2122 for TradeMark ™ 
  Input:
    No input required
  Output:
    UNIX® and Sun Microsystem™ are Copyright ©, 2019 Oracle
"""
#Print the  string as it is 
print("UNIX\u00AE and Sun Microsystem\u2122 are Copyright \u00A9,2019 Oracle ")
