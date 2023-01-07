# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:23:57 2022

@author: User
"""

def  main ():
  i = 1
  Input = int(input("Choose a number: "))
  value = i*Input
  while value<100:
    print(i,"*",Input,"=",i*Input)
    i = i+1
    value = i*Input
  print(i,"*",Input,"=",i*Input)

if  __name__  ==  "__main__" :
  main ()