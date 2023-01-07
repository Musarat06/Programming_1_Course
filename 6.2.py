# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:58:14 2022

@author: User
"""


def main():
  vow = ['a', 'e', 'i', 'o', 'u','y']
  Cons = ['z','b','t','g','h']
  vowel = 0
  con = 0
  word = input("Enter a word: ")
  for i in word:
    if i in vow:
      vowel = vowel+1
  con = con+(len(word)-vowel)

  print(f"The word \"{word}\" contains {vowel} vowels and {con} consonants.")

if __name__ == "__main__":
    main()