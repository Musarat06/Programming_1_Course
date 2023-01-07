# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:12:56 2022

@author: User
"""

def calculate_angle(angleA,angleB=90):
  """ Calculating the magnitude of angle of a traingle """

  Angle = 180-(angleA+angleB)

  return Angle

    
def main():
  angleA = int(input())
  angleB = int(input())
  print(calculate_angle(angleA,angleB))



if __name__ == "__main__":
  main()