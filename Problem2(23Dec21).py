"""
Problem 2:
Write a Python program to get the following from integer list of numbers from 1 to 100
(a) largest number from a list
(b) smallest number from a list
(c) prime number from a list
(d) Multiples of 10
"""


int_list=[i for i in range(1,101)]
#print(int_list)
#(a) largest number from a list
max_num=max(int_list)
print("largest number from a list is",max_num)


#(b) smallest number from a list
min_num=min(int_list)
print("smallest number from a list is",min_num)


#(c) prime number from a list
prime_list=[]
for i in int_list:
    if i>1:
        for j in range(2,i):
            #print(j)
            if(i%j)==0:
                break
        else:
            prime_list.append(i)
print(prime_list)



#(d) Multiples of 10
mul_10=[i for i in int_list if "0" in str(i)]
print(mul_10)