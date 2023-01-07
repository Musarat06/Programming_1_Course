# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 19:44:05 2022

@author: Musarat
"""
def main():
    Amount = float(input("Enter the amount of the study benefits: "))
    print("If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be",((1.17/100)*Amount)+Amount,"euros")
    print("and if there was another index raise, the study\nbenefits would be as much as",((2.17/100)*Amount)+Amount,"euros")
if __name__=="__main__":
    main()