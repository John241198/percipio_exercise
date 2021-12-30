"""
Problem 2:
You are given an list of floating point numbers.
(a) Find out the sum of maximum and minimum elements in the array.
(b) Average of all elements
(c) Plot a line graph using number of elements in x axis and the values corresponding to them in y axis
Use a list with minimum of 20 elements
Sample list = [10.11, 4.32, 5.764, 8.987]
"""
list = [10.11, 4.32, 5.764, 8.987]
#(a) Find out the sum of maximum and minimum elements in the array.
listmax = []
listmin = []
for number in list:
    if number > min(list):
        listmax.append(number)
for number in list:
    if number < max(list):
        listmin.append(number)
maxnum = sum(listmax)
minnum = sum(listmin)
print ("min sum:",round(minnum,2),"\nmax sum:",round(maxnum,2))


#(b) Average of all elements
avg_list=sum(list)/len(list)
print("Average :",round(avg_list,2))


#(c) Plot a line graph using number of elements in x axis and the values corresponding to them in y axis Use a list with minimum of 20 elements
import matplotlib.pyplot as plt
import random
x=[i for  i in range(1,21)]
y=[i for i in range(1,21)]
random.shuffle(y)

plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Line Graph!...')
plt.show()