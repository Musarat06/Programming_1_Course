# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:53:29 2022

@author: User
"""

def main():
    
    dates = []
    increment = 7
    for i in range(1, 13):
        if (i == 1):
            for j in range(3, 32, increment):
                dates.append(j)
                print("{}.{}.".format(j,i))
        elif (i == 3):
            for j in range(dates[-1] + increment - 28, 32, increment):
                dates.append(j)
                print("{}.{}.".format(j,i))
        elif (i == 5 or i == 7 or i == 8 or i == 10 or i == 12):
            for j in range(dates[-1] + increment - 31, 32, increment):
                dates.append(j)
                print("{}.{}.".format(j,i))
        elif (i == 2):
            for j in range(dates[-1] + increment - 31, 29, increment):
                dates.append(j)
                print("{}.{}.".format(j,i))
        else:
            for j in range(dates[-1] + increment - 29, 31, increment):
                dates.append(j)
                print("{}.{}.".format(j,i))
        


if __name__ == "__main__":
    main()