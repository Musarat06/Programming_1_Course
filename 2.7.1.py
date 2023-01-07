# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:19:51 2022

@author: Musarat
"""

def  main ():
  Num = int(input("How many Fibonacci numbers do you want? "))
  lis = list(range(1,Num+1))
  lis2 = []
  lis2.append(lis[0])
  lis2.append(lis[0])

  for i in range(Num):
    value = lis2[i]+lis2[i+1]
    lis2.append(value)
    print(f"{i+1}.",lis2[i])
 
if  __name__  ==  "__main__" :
  main ()