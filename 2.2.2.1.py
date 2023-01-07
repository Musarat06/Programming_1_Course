# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 18:53:15 2022

@author: Musarat
"""

def  main (): 
  while True:
    Input = input("Answer Y or N: ")
    if (Input=="Y" or Input=="N" or Input=="n"or Input=="y"):
      print("You answered",Input)
      break
      True
    else:
      print("Incorrect entry.")

if  __name__  ==  "__main__" : 
    main ()