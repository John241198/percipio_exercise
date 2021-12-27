# Problem 2
"""
Compress set of files in a local directory using compression tools in your system (eg: 7zip).
Display the pre and post size and % of reduction of file size
"""

import os
import subprocess


# file size before comp
filepath = r"C:\Users\ELCOT\HCL Python Training\john\multiple files"
before_size = 0
for i in os.listdir(filepath):
    file = os.path.join(filepath, i)
    before_size += os.path.getsize(file)
print("Before compress folder size:", before_size, "bytes")

comp_app = r"C:\Program Files\WinRAR\WinRAR.exe"
file = subprocess.Popen([comp_app, filepath])

# file size after comp
after_file = r"C:\Users\ELCOT\HCL Python Training\john\neww_dd"
after_size = 0
for i in os.listdir(after_file):
    file = os.path.join(after_file, i)
    after_size += os.path.getsize(file)
print("After compress folder size:", after_size, "bytes")

# percentage of reduced
diff = before_size - after_size
percentage = round(diff / before_size * 100)
print("Percentage of reduced size is :" + str(percentage) + "%")