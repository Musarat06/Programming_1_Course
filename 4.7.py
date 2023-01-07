# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 13:36:02 2022

@author: Musarat
"""

def Factorial(a):
  """ Finding the factorial of a fuction"""
  Product = 1
  for i in range(1,a+1):
    Product = Product*i
  return Product

def Probability(TotalBalls,Draw):
  """ Fuction the correct chances using the combination"""
  if TotalBalls>0 and Draw>0 and Draw<=TotalBalls:
    Answer = int(((Factorial(TotalBalls))/(Factorial(TotalBalls-Draw)*Factorial(Draw))))
    print(f'The probability of guessing all {Draw} balls correctly is {1}/{Answer}')
  

def main():
  while True:
    TotalBalls = int(input("Enter the total number of lottery balls: "))
    Draw = int(input("Enter the number of the drawn balls: "))
    if TotalBalls<0 or Draw<0:
      print("The number of balls must be a positive number.")
      break
      
    elif Draw>TotalBalls:
      print("At most the total number of balls can be drawn.")
      break
    else:
      break
  Probability(TotalBalls, Draw)

if __name__ == "__main__":
    main()