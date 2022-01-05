"""
Problem4: Using regular expression pattern matching, check if there is a URL in the given file -
You can use the GNU licence file which we had used earlier
https://www.gnu.org/licenses/gpl-3.0.txt
"""

import re
file=open(r'C:\Users\ELCOT\HCL Python Training\john\GPL_Local_File.txt').read()
print("urls in GPL_Local_File.txt:")
for i in re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))[^>]+',file):
    print(i)