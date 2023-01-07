# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:15:32 2022

@author: User
"""

def capitalize_initial_letters(string):
  """ This fucction is used to capitalize the first letter of each word."""
  return string.title()


def main():
  string = 'centrali ntelligence ageAcy'
  name = capitalize_initial_letters(string)
  print(name)

if __name__ == "__main__":
    main()