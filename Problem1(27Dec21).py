#Prblem 1
"""
Solve using subprocess
(a) List the files present in C:\Windows directory - observe the use of SHELL parameter set to True and False
(b) Write a python program to Check if notepad program is present in the system. Execute that program using subprocess
(c) Write a batch program  to find the count of number of files and directories inside C:\Windows directory. Call that
program using subprocess and display the output.

Prepare a document mentioning in detail about subprocess module.
Only add information which you understand and have used in the programs.
"""

import os
import subprocess

#(a) List the files present in C:\Windows directory - observe the use of SHELL parameter set to True and False
file_dir=subprocess.run("dir",shell=True)
print(file_dir)

#file_dir=subprocess.run("dir",shell=False)
#print(file_dir)

#file_dir=subprocess.run("dir",shell=True,capture_output=True,text=True)
#print(file_dir.stdout)


print()
#(b) Write a python program to Check if notepad program is present in the system. Execute that program using subprocess
python=r"C:\Users\ELCOT\AppData\Local\Programs\Python\Python38\python.exe"
file_dir1=subprocess.run([python,r"C:\Users\ELCOT\HCL Python Training\john\file_exist.py"],shell=True,capture_output=True,text=True)
print(file_dir1.stdout)


#(c) Write a batch program  to find the count of number of files and directories inside C:\Windows directory. Call that program using subprocess and display the output.

p4=subprocess.run([python,r"C:\Users\ELCOT\HCL Python Training\john\count.py"],shell=True,capture_output=True,text=True)
print(p4.stdout)