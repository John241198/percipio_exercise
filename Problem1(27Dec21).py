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




"""
Prepare a document mentioning in detail about subprocess module. 
Only add information which you understand and have used in the programs
"""

"""
subprocess module:
    
    i)shell parameter:
        when shell=True it will display shell commands result/shell=False (default) at certain point the system
        could not find the file specified or path is not found reason is the command used in the above program is 
        "dir" which is build in the shell command so we have to pass shell argument in run process
            example:
                subprocess.run("dir",shell=True)
                
    ii)standard out(stdout):
        when we complete the process it will display "completed process(arg["dir"],returncode=0)" 
        example:
            p1=subprocess.run("dir",shell=True)
            print(p1.args) it output is "dir"
            print(p1.returncode) its output is 0(sucessful)
            print(p1.stdout) is output is None
            
            because we have to capture output using capture_output=True argument must pass in the subprocess program
        now we print(p1.stdout) output will be in bytes to decode that we use stdout.decode() methods to display
        exact command will shows in the console windows also we can pass text=True argument and instant of decode.
        
"""
