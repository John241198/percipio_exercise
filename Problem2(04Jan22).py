"""
Problem 2: Program for removing i-th character from a string
Given a string - ""Python"" - Index starts from 0, User input to be taken for the input string and index to be removed
if 1 is the index to be removed - output will be ""Pthon""
"""
user_input=list(input("enter the string:"))
try:
    remove_index=int(input("Enter index position to remove:"))
    remove=user_input.remove(user_input[remove_index])
    print("Output string:","".join(user_input))

except IndexError:
    print("IndexError: list index out of range\nEnter required index need to be remove!..")
except ValueError:
    print("Enter integer value only!...")