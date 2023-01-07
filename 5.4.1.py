# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:44:06 2022

@author: User
"""

def main():
  Num = int(input("How many numbers do you want to process: "))
  print("Enter",Num,"numbers:")
  count = 0
  InNumberList = []
  while count<Num:
    InNum = int(input())
    InNumberList.append(InNum)
    count = count+1
  SearchNumber = int(input("Enter the number to be searched: "))
  Count = InNumberList.count(SearchNumber)
  if Count==0:
    print(SearchNumber,"is not among the numbers you have entered.")
  else:
    print(SearchNumber,"shows up",Count,"times among the numbers you have entered.")


if __name__ == "__main__":
    main()