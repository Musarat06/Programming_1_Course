# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:00:15 2022

@author: User
"""

def create_an_acronym(string):
  """ This fucction is used to fid the acronyms of the user input string."""
  acro = string[0]
  for i in range(1,len(string)):
    if string[i-1]==' ':
      acro += string[i]
  return acro.upper() 

def main():
  string = 'centrali ntelligence agency'
  name = create_an_acronym(string)
  print(name)

if __name__ == "__main__":
    main()