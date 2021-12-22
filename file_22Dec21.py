def program():
    print("""press 1 for Greater than two Problem\n
             press 2 for Bike cheap problem\n
             press 3 for trip restriction guide\n
             press 4 for online shipping scinario\n
             press 5 for number which are divisible by 2\n
             press 6 for appending numbers div by 3 or 5 in the list\n
             press 7 for maths table (1-10)\n
             press 8 for square root of number also use break statement\n
             press 9 for prime number\n
             press 10 for creating password authentication\n
             press 11 for check alphabet count and digit count in the string\n
             press 12 for password authentication(while loop)\n
             press 13 for number of times to print string\n
             press 14 for find the number of digits in an integer\n
             press 15 for appending odd and even number in a list using while loop\n
             press 16 for cube root of number\n
             press 17 for finding number of vowels and consonants in a string\n
             
             """)

    option = int(input("Enter the option: "))

    if option == 1:
        #Greater than two Problem
        n = int(input("Enter the number : "))
        if n > 2:
            print("Greater!...")
        else:
            print("Less than 2")

    elif option == 2:
        #Bike cheap problem
        bike = 3000
        if bike < 3000:
            print("It is cheep bike")
        elif bike >= 3000 or bike < 4000:
            print("Bike is some more cheep")
        elif bike >= 4000:
            print("Bike is expensive")

    elif option == 3:
        #trip restriction guide
        age = int(input("Enter age : "))
        if age >= 15:
            if age > 20:
                print("Too old for this trip!..")
            else:
                print("right age for this trip!..")
        else:
            print("you are too young for this trip!..")

    elif option==4:
        #online shipping scinario
        total = int(input("What is the total amount of your shppping ? "))
        country = input("USA or CANADA? ")

        if country == "USA":
            if total <= 50:
                print("shipping cost is $9.00")
            elif total <= 100:
                print("shipping cost is $6.00")
            else:
                print("shipping is free!...")

        if country == "CANADA":
            if total <= 50:
                print("shipping cost is $12.00")
            elif total <= 100:
                print("shipping cost is $8.00")
            else:
                print("shipping is free!...")


    elif option==5:
        #number which are divisible by 2
        for i in range(1, 10 + 1):
            if i % 2 == 0:
                print(i, " is divisible by 2")
            else:
                print(i, " is not divisible by 2")

    elif option==6:
        #appending numbers div by 3 or 5 in the list
        n = []
        for i in range(1, 21):
            if i % 3 == 0 or i % 5 == 0:
                n.append(i)
        print(n)


    elif option==7:
        # maths table (1-10)
        for i in range(1, 10):
            print("num = ", i, ":", end=" ")
            for j in range(1, 10):
                print("{}".format(i * j), end=" ")
            print()

    elif option==8:
        #square root of number also use break statement
        for i in range(1, 10):
            if i ** 2 > 20:
                break
            print(i, " is square of ", i ** 2)

    elif option==9:
        #prime number
        n = int(input("Enter the number: "))
        for i in range(2, n):  # here prime numers are greater tha 2 so we start range with 2
            if n % i == 0:
                print("Not prime")
                break  # here if statement is true it breaks and print else
        else:
            print("prime")

    elif option==10:
        #creating password authentication
        for i in range(3):
            p = str(input("Enter pass : "))
            if p == "123":
                print("welcome!....")
                break
        else:
            print("3 incorrect password attempt")

    elif option==11:
        #check alphabet count and digit count in the string
        string = str(input("Enter the string "))
        digit = 0
        alpha = 0

        for i in string:
            if i.isdigit():
                digit += 1
            elif i.isalpha():
                alpha += 1

        print("digits in string ", digit)
        print("alphabet in string ", alpha)

    elif option==12:
        #creating password authentication
        password = " "

        while password != "John@123":
            password = str(input("enter the password: "))
        print("Access graneded!....")


    elif option==13:
        n = int(input("Enter the number of time to print string: "))
        s = input("Enter the string to print: ")

        c = 1
        while c <= n:
            print(c, ":", s)
            c += 1

    elif option==14:
        #find the number of digits in an integer
        val = int(input("Enter the integer: "))
        digit = 0

        while val > 0:
            val //= 10
            digit += 1

        print("num digit: ", digit)

    elif option==15:
        #appending odd and even number in a list using while loop
        even = []
        odd = []
        i = 1
        while i <= 20:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
            i += 1

        print(even)
        print(odd)

    elif option==16:
        #cube root of number
        while True:
            v = input("enter number: ")
            if v == 'out':
                print("bye!...(loop exist using break)")
                break
            if not v.isdigit():
                print("Enter the integer only!")
                continue
            v = int(v)
            print("cube of %d is %d " % (v, v ** 3))

    elif option==17:
        n = input("enter a string: ")
        vowels = 0
        consonants = 0

        for i in n:
            if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
                    i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
                vowels = vowels + 1  # vowel counter is incremented by 1
            else:
                consonants = consonants + 1
        # consonant counter is incremented by 1
        print("The number of vowels:", vowels)
        print("The number of consonant:", consonants)

    else:
        return "Incorrect option"