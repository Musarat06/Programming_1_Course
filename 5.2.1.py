# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 21:02:00 2022

@author: Musarat
"""

def  main (): 
  Num = [x for x in range(101)]
  even = []
  for i in Num:
    if i%2==0:
      even.append(i)
  for num in reversed(even):
    even.append(num)
  print(*even,sep='\n')

if  __name__  ==  "__main__" : 
    main () 