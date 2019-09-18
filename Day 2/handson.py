# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:53:43 2019

@author: de
"""


# Hands On 1
string = "Rajasthan"

#Print characters at the even index number 
print(string[0::2])

# Hands On 2
string = "Rajasthan"

#Print the given string in reverse 
print(string[::-1])
print(string[-1::-1])

# Hands On 3
string = "Forsk Technologies"
#Print Forsk using slicing ( forward indexing Left to Right  )  
print(string[0:5])

# Hands On 4
string = "Forsk Technologies"
#Print Technologies using slicing ( forward indexing Left to Right )  
string[6:]

# Hands On 5
string = "Forsk Technologies"
#Print Forsk using slicing ( Reverse indexing Right to Left  )  
string[-19:-13]

# Hands On 6
string = "Forsk Technologies"
#Print Technologies using slicing ( forward indexing Right to Left )  
string[-12:]

# Hands On 7
string = "Forsk Technologies"
#Print ksroF using slicing ( forward indexing Left to Right  )  
string[4::-1]

# Hands On 8
string = "Forsk Technologies"
#Print siesgolonhceT using slicing ( forward indexing Left to Right )  
string[19:5:-1]

# Hands On 9
string = "Forsk Technologies"
#Print Technologies Forsk using slicing ( forward indexing Left to Right  ) 
print(string[6:20] + " " + string[0:5] )
