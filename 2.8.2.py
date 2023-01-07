# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:53:12 2022

@author: Musarat
"""

def main():
  for i in range(1, 13):
    if (i==4 or i==6 or i==9 or i==11):
      for j in range(1, 31):
        print("{}.{}.".format(j,i))
    elif i==2:
      for j in range(1,29):
        print("{}.{}.".format(j,i))
    else:
      for j in range(1,32):
        print("{}.{}.".format(j,i))
if __name__ == "__main__":
    main()