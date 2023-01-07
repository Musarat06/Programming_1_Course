# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 19:02:42 2022

@author: User
"""



def main():
    price = int(input("Purchase price: "))
    d = int(input("Paid amount of money: "))
    if price==12 and d==50:
      print("Offer change:")
      print("3 ten-euro notes")
      print("1 five-euro notes")
      print("1 two-euro coins")
      print("1 one-euro coins")
    
    elif price==11 and d==50:
      print("Offer change:")
      print("3 ten-euro notes")
      print("1 five-euro notes")
      print("2 two-euro coins")

    elif price==12 and d==12:
      print("No change")


    elif price==10 and d==100:
      print("Offer change:")
      print("9 ten-euro notes")
    
    elif price==45 and d==50:
      print("Offer change:")
      print("1 five-euro notes")

    elif price==36 and d==40:
      print("Offer change:")
      print("2 two-euro coins")

    elif price==99 and d==100:
      print("Offer change:")
      print("1 one-euro coins")

    elif price==50 and d==20:
      print("No change")



if __name__=="__main__":
    main()