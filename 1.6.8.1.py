# -*- coding: utf-8 -*-
"""

@author: Musart
"""





def main():
    Player1 = input("Player 1, enter your choice (R/P/S): ")
    Player2 = input("Player 2, enter your choice (R/P/S): ")
    if Player1=="P" and Player2=="S":
      print("Player 2 won!")
    elif Player1=="P" and Player2=="R":
      print("Player 1 won!")

    elif Player1=="R" and Player2=="S":
      print("Player 1 won!")

    elif Player1=="S" and Player2=="S":
      print("It's a tie!")


if __name__=="__main__":
    main()