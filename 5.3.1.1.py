# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:40:27 2022

@author: User
"""

def  main ():
  print("Give 5 numbers:")
  i = 1
  Num = []
  while i<6:
    Input = int(input("Next number: "))
    i = i+1
    Num.append(Input)

  print("The numbers you entered that were greater than zero were:")
  for i in Num:
    if i>0:
      print(i)
 
if  __name__  ==  "__main__" :
  main ()