#!/usr/bin/python3
"""
Make a program that takes a string S and an integer N as
argument and print the list of words in S that contains
more than N non-punctuation characters.

• Words are separated from each other by space characters
• Punctuation symbols must be removed from the printed list: they are neither part
of a word nor a separator
• The program must contains at least one list comprehension expression.
If the number of argument is different from 2, or if the type of any argument is wrong,
the program prints an error message.
"""

import sys


def fil_list(words, leng):
    print(words, leng)
    words_list = words.split() 
:
if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args == 1 or num_args > 3:
        print("ERROR")
    elif sys.argv[2].isnumeric():
        fil_list(sys.argv[1], sys.argv[2])
    else:
        print("ERROR")
