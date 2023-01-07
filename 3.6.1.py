"""
COMP.CS.100 Programming 1
Template Song: Old MacDonald
"""
def print_verse(str1,str2):
  """ This fuction take two string and then pring line using these string in their lines"""
  print("Old MACDONALD had a farm")
  print("E-I-E-I-O")
  print("And on his farm he had a {}".format(str1))
  print("E-I-E-I-O")

  print("With a {} {} here".format(str2,str2))
  print("And a {} {} there".format(str2,str2))
  print("Here a {}, there a {}".format(str2,str2))
  print("Everywhere a {} {}".format(str2,str2))
  print("Old MacDonald had a farm")
  if str1 == 'lamb':
    print("E-I-E-I-O")
  else:
    print("E-I-E-I-O\n")


def main():
    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")

if __name__ == "__main__":
    main()