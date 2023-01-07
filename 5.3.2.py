# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:29:26 2022

@author: User
"""

def main():
  count = 1
  Number = []
  print("Give 5 numbers:")
  while count <6:
    Num = int(input("Next number: "))
    Number.append(Num)
    count = count+1
  Number.reverse()
  print("The numbers you entered, in reverse order:")
  for i in Number:
      print(i)

if __name__ == "__main__":
    main()