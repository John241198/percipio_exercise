"""
Problem 1: Permutations
Find all possible permutations of the input string (single word).
Consider each alphabet is unique.
For Eg: Input is abc
Output should be
abc
acb
bac
bca
cab
cbc
"""

from itertools import permutations

input_string=str(input("Enter the string:"))

if input_string.isalpha():
    permutation=permutations(input_string,len(input_string))
    for i in permutation:
        print("".join(i))
else:
    print("Enter the alphabet only!....")