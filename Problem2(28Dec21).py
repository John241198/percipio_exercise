"""
Problem 2: Jumping Numbers
A number is a jumping number when all the adjacent digits have difference of 1.
Eg: 23, 45, 4343456
Write a program to find all jumping numbers less than the given input number.
If input is 50 - Jumping numbers will be 10, 12, 23, 32, 34, 43, 45,
"""

try:
    n=int(input('Enter the Number:'))

    for i in range(n):
        """
        if (i<11):
            print(i,end=' ')
            continue
            """

        if(i<100):
            digit1=i%10
            digit2=i//10
            if(abs(digit1-digit2)==1):
                print(i,end=" ")
        elif(i>100 and i<1000):
            temp=i
            digit1=i%10
            temp=temp//10
            digit2=temp%10
            temp=temp//10
            digit3=temp%10
            if(abs(digit1-digit2)==1 and abs(digit2-digit3)==1):
                print(i,end=" ")
except ValueError:
    print("Enter integer value only!....")