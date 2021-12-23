"""
Problem 1:
Write a Python program to sort (ascending and descending) a dictionary by value.
Sample dictionary - d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
Try with different types of dictionary elements
"""


d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b={"A":4,"B":3,"C":5,"D":2}


def Dict_ascending(n):
    list_order=dict(sorted(n.items(),key=lambda item:item[1]))  #sorted(iterable,key=None,reverse=False)
    return list_order

def Dict_descending(n):
    list_order=dict(sorted(n.items(),key=lambda item:item[1],reverse=True))
    return list_order

print("Ascending order(dictionary by value):",Dict_ascending(b))
print("Descending order(dictionary by value):",Dict_descending(b))