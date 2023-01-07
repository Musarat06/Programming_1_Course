# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:26:19 2022

@author: User
"""

def main():
  i = 1
  InputTimeList = []
  while i<6:
    InputTime = float(input(f"Enter the time for performance {i}: ".format(i)))
    InputTimeList.append(InputTime)
    i = i+1

  maxi = max(InputTimeList)
  mini = min(InputTimeList)
  InputTimeList.remove(maxi)
  InputTimeList.remove(mini)
  N = len(InputTimeList)
  sum = 0
  for elem in InputTimeList:
    sum = sum+elem
  
  average = sum/N
  print("The official competition score is",round(average,2),"seconds.")


if __name__ == "__main__":
  main()