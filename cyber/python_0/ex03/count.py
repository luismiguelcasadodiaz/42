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

def format_output(tot: int, up: int, lo: int, pu: int, sp: int):
    print("The text contains {} character(s):".format(tot))
    print("- {} upper letter(s)".format(up))
    print("- {} lower letter(s)".format(lo))
    print("- {} punctuation mark(s)".format(pu))
    print("- {} space(s)".format(sp))

def text_analyser(arg: str):
    """
    PARAMETERS
        a text string to make statisics on it

    RETURNS
        nothing


    """
