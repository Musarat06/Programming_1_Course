# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:19:58 2022

@author: User
"""

def reverse_name(string):
  """ This fucction is used to reverse the order of the name given by the user."""
  
  try:
    string = string.strip()
    last, first = string.split(",")
    last = last.strip()
    first = first.strip()
    name = first+' '+last
  except:
    name = string.strip()
  return name.strip()

def main():
  string = 'X,'
  name = reverse_name(string)
  print(name)

if __name__ == "__main__":
    main()