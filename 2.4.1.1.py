# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:34:02 2022

@author: Musarat
"""

def  main ():
  Num = int(input("How many numbers would you like to have? "))
  for i in range(1,Num+1):
    if i%3==0 and i%7==0:
      print("zip boing")

    elif i%3==0:
      print("zip")
    elif i%7==0:
      print("boing")
    else:
      print(i)

 
if  __name__  ==  "__main__" :
  main ()