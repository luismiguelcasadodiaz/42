#!/usr/bin/python3
""" Create a function called text_analyzer
    that takes a single string argument and displays
    the sums of its
    upper-case characters,
    lower-case characters,
    punctuation characters and
    spaces.
    • If None or nothing is provided
        the user is prompted to provide a string.
    • If the argument is not a string
        print an error message.
    • This function must have a docstring explaning its behavior.
"""


import string
import sys


def format_output(tot: int, up: int, lo: int, pu: int, sp: int):
    print("The text contains {} character(s):".format(tot))
    print("- {} upper letter(s)".format(up))
    print("- {} lower letter(s)".format(lo))
    print("- {} punctuation mark(s)".format(pu))
    print("- {} space(s)".format(sp))


def counter(arg: str):
    # counters set up
    tot = len(arg)
    up = 0
    lo = 0
    pu = 0
    sp = 0
    for i in range(tot):
        if arg[i].isupper():
            up = up + 1
        elif arg[i].islower():
            lo = lo + 1
        elif arg[i] in string.punctuation:
            pu = pu + 1
            print("--",arg[i])
        elif arg[i].isspace():
            sp = sp + 1

    format_output(tot, up, lo, pu, sp)





def text_analyser(*arg):
    """
    This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text.
    PARAMETERS
        a text string to make statisics on it
    RETURNS
        nothing
    """
    print(arg)
    if  isinstance(arg[0], int):
        raise AssertionError("argument is not a string")
    correct_arg = False
    while not correct_arg:
        if arg is None or arg == "":
            arg = input("Please enter the text to analuse:").strip()
            if len(arg) != 0:
                correct_arg = True
        else:
            correct_arg = True
    counter(arg)

if __name__ == "__main__":
    num_args = len(sys.argv)
    if num_args > 2 or num_args == 1:
        print("Usage is: count.py <string>")
        sys.exit(-1)
    else:
        text_analyser(sys.argv[1])
