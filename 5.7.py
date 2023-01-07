# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:09:38 2022

@author: User
"""


def main():
  Sch = [630, 1015,1415,1620,1720,2000,630,1015,1415]
  BusTime = int(input("Enter the time (as an integer): "))
  i = 0
  for ind,val in enumerate(Sch):
    if val>=BusTime:
      i = i+1
      print("The next buses leave:")
      print(val)
      print(Sch[ind+1])
      print(Sch[ind+2])
      break
    else:
      i = i+1
    
    if i>8:
      print("The next buses leave:")
      print(Sch[0])
      print(Sch[1])
      print(Sch[2])
      break

if __name__ == "__main__":
    main()