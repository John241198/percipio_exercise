"""
Problem 1: Check if a Substring is Present in a Given String

Eg: If input is ""Substation"" - we can check for the presence of substring - ""sub"" or ""station"".
    Write few lines as input which has repeating substrings and validate your program
"""

string="""here is my substring with substation present in the given string we need to find substation
          here is my substring with substation present in the given string we need to find substation
          here is my substring with substation present in the given string we need to find substation"""


sub_str=str(input("Enter the sub_string to find:"))
if sub_str.isalpha():
    if(string.find(sub_str)==-1):
        print("Not Present in the string")
    else:
        print("Present in the string")
else:
    print("Enter the alphabet only to find substring!...")
