# -*- coding: utf-8 -*-
"""

@author: User
"""
def  main (): 
    age  =  int(input("Please, enter your age: "))

    if  age  <  25 and age>16:
      ticket_price  =  1.47 
    elif  age  <  17 and age>6:
      ticket_price  =  1.02 
    elif  age  <  7 and age>0:
      ticket_price  =  0.00 
    else: 
      ticket_price  =  2.04 

    print ("Your ride will cost:",ticket_price ) 


if  __name__  ==  "__main__" : 
    main () 

