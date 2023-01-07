# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:05:16 2022

@author: User
"""

def is_the_list_in_order(Lis):
  ''' This function take list as input and print True if all element are in order and false in other way '''
  if len(Lis)>1:
    chk = True

    if Lis != sorted(Lis):
      chk = False

  else:
    chk = True  
  return chk==True
                       


def main():
    Lis = [1, 2, 3, 6, 5, 6]
    print(is_the_list_in_order(Lis)==True)


if __name__ == "__main__":
  main()