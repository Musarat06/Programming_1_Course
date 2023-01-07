# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:01:34 2022

@author: Musarat
"""

def  main (): 
  Input = int(input("Choose a number: "))
  lis = [1,2,3,4,5,6,7,8,9,10]
  for i in lis:
    print(i,"*",Input,"=",i*Input)

if  __name__  ==  "__main__" : 
    main ()