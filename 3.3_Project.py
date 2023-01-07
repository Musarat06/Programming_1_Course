# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:39:05 2022

@author: Musarat
"""

def  main (): 
  month = 1
  Inflation = []
  while True:
    Md = input(f'Enter inflation rate for month {month}: ')
    if Md=='':
      break
    else:
      Md = float(Md)
      Inflation.append(Md)
      month = month+1
  lenInflation = len(Inflation)
  if lenInflation<2:
    print("Error: at least 2 monthly inflation rates must be entered.")
  else:
    maxlist = []
    for i in range(len(Inflation)-1):
      val = Inflation[i+1]-Inflation[i]
      maxlist.append(val)
    Maximum = round(max(maxlist),1)
    print("Maximum inflation rate change was",Maximum,"points.")

if  __name__  ==  "__main__" : 
    main ()