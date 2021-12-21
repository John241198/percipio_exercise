#percipio condition statements & baisc loops

"""
question:If a number is greater than 2 print greater or not greater
approach:using if else condition
"""

n=int(input("Enter the number : "))
if n>2:
    print("Greater!...")
else:
    print("Less than 2")





"""
question:find the bike price is cheap or some more cheap or expensive
approach:using if elif condition statements
"""


bike=3000

if bike<3000:
    print("It is cheep bike")
elif bike>=3000 or bike<4000:
    print("Bike is some more cheep")
elif bike>=4000:
    print("Bike is expensive")






"""
question:trip restriction guide
approach:using nested if else condition
"""

age=int(input("Enter age : "))
if age>=15:
    if age>20:
        print("Too old for this trip!..")
    else:
        print("right age for this trip!..")
else:
    print("you are too young for this trip!..")







"""
question :online shipping scinario based on country and customer shopping offers 
approach:get input from user and perform if else condition statements
"""

total=int(input("What is the total amount of your shppping ? "))
country=input("USA or CANADA? ")

if country == "USA":
    if total<=50:
        print("shipping cost is $9.00")
    elif total <=100:
        print("shipping cost is $6.00")
    else:
        print("shipping is free!...")

if country=="CANADA":
    if total<=50:
        print("shipping cost is $12.00")
    elif total<=100:
        print("shipping cost is $8.00")
    else:
        print("shipping is free!...")






#percipio advance operation using for loop
"""
question : printing number which are divisible by 2
approach : using range function getting input through for loop and inside for we 
perform if else condition for number divisible by 2  
"""

for i in range(1,10+1):
    if i%2==0:
        print(i," is divisible by 2")
    else:
        print(i," is not divisible by 2")




"""
question:appending numbers div by 3 or 5 in the list
approach: get input from range fun through for loop and perform if condition 
and using append method we append in list and print appended list
"""

n=[]
for i in range(1,21):
    if i%3==0 or i%5==0:
        n.append(i)
print(n)






"""
question : maths table (1-10)
approach : using for loop getting input from range function and we perform multiplication using 
another for loop(nested for-loop) and printing values using format function 
"""

for i in range(1,10):
    print("num = ",i,":",end=" ")
    for j in range(1,10):
        print("{}".format(i*j),end=" ")
    print()
    





"""
question: square root of number also use break statement
approach:using for loop getting input and print square root condition in if-else statement also 
using certain if-else condition gets True it break the loop using break statement
break statement - when used inside the loop it will terminate loop and exist and if we use inside
the nested loop it will break out from the current loop
"""

for i in range(1,10):
    if i**2>20:
        break
    print(i," is square of ",i**2)






"""
question:prime number
"""

n=int(input("Enter the number: "))
for i in range(2,n): #here prime numers are greater tha 2 so we start range with 2
    if n%i==0:
        print("Not prime")
        break#here if statement is true it breaks and print else
else:
    print("prime")





"""
question : creating password authentication 
approach : using for loop 3attempts can try get user pass if password is crt it 
will print statement and break for loop using break statement else it continue for 
password check for loop exit and print else statements
"""

for i in range(3):
    p=str(input("Enter pass : "))
    if p=="123":
        print("welcome!....")
        break
else:
    print("3 incorrect password attempt")







"""
question :check alphabet count and digit count in the string
approach :get the str in forloop and check with if-else  condition for digit use isdigit() to check digit 
increment digit and if alphabet use isalpha() in elif and increment alpha  and print digit and alpha counts 
"""

string=str(input("Enter the string "))
digit=0
alpha=0

for i in string:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1


print("digits in string ",digit)
print("alphabet in string ",alpha)








#percipio while loop
"""
question : password authentication 
approach:using while loop initialize empty variable and perform input statements from the user
if the while condition false it will break the statement and print the access 
"""

password=" "

while password != "John@123":
    password=str(input("enter the password: "))
print("Access graneded!....")



"""
question:number of times to print string
approach:get input for number of time to print and number of time to print string
from user using while loop printing the string as per input value
"""

n=int(input("Enter the number of time to print string: "))
s=input("Enter the string to print: ")

c=1
while c<=n:
    print(c,":",s)
    c+=1







"""
question:find the number of digits in an integer
approach:get integer val and initalize variable as zero and perform while loop
while true it will perform floor division(//) get increment until the while loop
exist
"""

val=int(input("Enter the integer: "))
digit=0

while val>0:
    val//=10
    digit+=1

print("num digit: ",digit)






"""
question:appending odd and even number in a list using while loop
approach:initialize empty list for even and odd and using while loop number to
print and condition to print with if-else condition append the number in empty lists 
"""

even=[]
odd=[]
i=1
while i<=20:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    i+=1

print(even)
print(odd)






"""
question:cube root of number
approach:using while loop get input from user and add some condition to check
number is valid for printing cube root usinf if-else conditon and also using break
and continue for exist loop
"""

while True:
    v=input("enter number: ")
    if v=='out':
        print("bye!...(loop exist using break)")
        break
    if not v.isdigit():
        print("Enter the integer only!")
        continue
    v=int(v)
    print("cube of %d is %d "%(v,v**3))




"""
question:finding number of vowels and consonants in a string
approach:
"""

n = input("enter a string: ")
vowels = 0
consonants = 0

for i in n:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
            i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1 # vowel counter is incremented by 1
    else:
        consonants = consonants + 1
# consonant counter is incremented by 1
print("The number of vowels:", vowels)
print("The number of consonant:", consonants)