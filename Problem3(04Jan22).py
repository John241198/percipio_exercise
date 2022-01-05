"""
Problem 3: Search and find a specific file in a  directory with several files.
Implement this using more than one way and try to understand the difference and uniqueness in each solution
"""

import os,re
mypath=r"C:\Users\ELCOT\HCL Python Training\john\multiple files"

search_file=input("Enter search file:")
for file_path in os.listdir(mypath):
    match = re.search(search_file, file_path)
    if match:
        print("file found!...")
        break
else:
    print("file not found!...")


#another method
"""
regex = re.compile('(^s.*txt$)')
for root, dirs, files in os.walk(mypath):
    for file in files:
        if regex.match(file):
            print("file found!...")
            break
    else:
        print("file not found!...")
"""