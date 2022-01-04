"""
Problem 2: Multithreading
Write a sample program to demonstrate multithreading in python
"""

"""
Threading---Threading in python is used to run multiple threads (tasks, function calls) at the same time..
"""



"""
class hello:

    def run(self):
        for i in range(5):
            print("hello")

class hi:

    def run(self):
        for i in range(5):
            print("hi")

task1=hello()
task2=hi()

task1.run()
task2.run()
"""


"""
here the out first function(run) declared the first output as hello then second function(run) output as hi
take certain time to print first function and second function now we can use the both function to perform 
simultanously to print both fun at same time by using  the "THREADING"

by default every execution has one thread that is "main-thread"the code execution has done by the default 
thread that is main thread to perform the two thread for two function we should made the thread to be sub-class 
for every function
"""
from time import sleep
from threading import *


class Hello(Thread):  # fun's sub-class//thread -need to import module "from threading import *"

    def run(self):  # run is inbuild method in thread if we call any other method it will not work
        for i in range(5):
            print("hello")
            sleep(1)  # without sleep it work too faster so we make sleep to print one fun to other fun with sleep()


class Hi(Thread):

    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


task1 = Hello()
task2 = Hi()

task1.start()  # if we want to run two different thread instant of calling run method we neet to call start()-method //when we call start() internaly it call run method
sleep(0.2)  # sometime two thread come in the cpu at same time and it will make collision
task2.start()

task1.join()
task2.join()

print("Completed!....")