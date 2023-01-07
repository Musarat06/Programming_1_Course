"""
COMP.CS.100 Programming 1
Print a box with input error checking
"""

def print_box(Width,height,mark):
  """ This fuction take width, height and mark and print mark as per the width and height"""
  for i in range(Width):
    print(mark*Width)
    break
  while height>1:
    print(mark*Width)
    height = height-1


def read_input(inputt):
  """ This fuciton take input string from user and return int value in ouput"""
  while True:
    UserInput = int(input(inputt))
    if UserInput>0:
      break
  return UserInput


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")

    mark =   input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()