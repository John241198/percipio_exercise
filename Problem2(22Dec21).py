"""
Write a python program to download file https://www.gnu.org/licenses/gpl-3.0.txt.

Save it in a predefined location Eg: <some local path>
Perform the following operations in the downloaded file:
a) Duplicate the file to another file named GPL_Local_File.txt

b) Count the total number of words

c) Count the number of occurrences of word "License", "free software" and "code"

d) Create a new file with the information from the output of (b) and (c)

"""

import requests
import os

url="https://www.gnu.org/licenses/gpl-3.0.txt"
request=requests.get(url)

with open(r"C:\Users\ELCOT\HCL Python Training\john\file22dec21.txt","wb") as file:
    file.write(request.content)
    with open(r"C:\Users\ELCOT\HCL Python Training\john\file22dec21.txt","r") as f,open(r"C:\Users\ELCOT\HCL Python Training\john\GPL_Local_File.txt","w") as f1:
        #a) Duplicate the file to another file named GPL_Local_File.txt
        for i in f:
            f1.write(i)
        with open(r"C:\Users\ELCOT\HCL Python Training\john\GPL_Local_File.txt","r") as f3:
            #b) Count the total number of words
            #c) Count the number of occurrences of word "License", "free software" and "code"
            data=f3.read()
            words=data.split()
            w1=len(words)
            w2=data.count("License")
            w3=data.count("free software")
            w4=data.count("code")
            print("Number of word in GPL_Local_File.txt :",len(words))
            print("License occurrences in GPL_Local_File.txt :",data.count("License"))
            print("free software occurrences in GPL_Local_File.txt :",data.count("free software"))
            print("code software occurrences in GPL_Local_File.txt :",data.count("code"))
            #d) Create a new file with the information from the output of (b) and (c)
            with open(r"C:\Users\ELCOT\HCL Python Training\john\Information.txt","w") as f4:
                f4.write("Number of word in GPL_Local_File.txt :"+str(w1)+"\n")
                f4.write("License occurrences in GPL_Local_File.txt :"+str(w2)+"\n")
                f4.write("free software occurrences in GPL_Local_File.txt :"+str(w3)+"\n")
                f4.write("code software occurrences in GPL_Local_File.txt :"+str(w4)+"\n")