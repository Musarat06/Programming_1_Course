# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 22:30:26 2022

@author: Musarat
"""

def are_all_members_same(Lis):
  ''' This function take list as input and print True if all element and False otherwise '''
  if len(Lis)>0:

    ele = Lis[0]
    chk = True

    for item in Lis:
      if ele != item:
          chk = False
          break;
  else:
    chk = True
    
  return chk==True
                       


def main():
    Lis = [1, 1, 1, 1, 1, 1]
    print(are_all_members_same([])==True)


if __name__ == "__main__":
  main()