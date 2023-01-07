# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:56:07 2022

@author: User
"""
def compare_floats(a, b, EPSILON):
  """ Take input values and return either false or true"""
  return abs(a-b)<EPSILON


def main():
  EPSILON = 0.0000000000001
  compare_floats(0.00000000000000000001, 0.0000000000000000002,EPSILON)

if __name__ == "__main__":
    main()