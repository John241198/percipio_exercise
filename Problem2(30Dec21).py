"""
Problem 2:
In a sentence, find out if there is a valid IP address and print the same.
Try solution with and without usage of regular expressions.
For example:
Input:
"The system's is accessed from 10.50.200.1"
output :
IP Address is 10.50.200.1
Total IP Address noted is 1
"""
ip="IP Address is 10.50.200.1 and also along with 10.50.200.1 also along with 10.50.200.1 also along with 10.50.200.1"


new_ip = ''.join((i if i in '0123456789.' else ' ') for i in ip)
ip_list=[]
for i in new_ip.split():
    ip_list.append(i)
    print("IP Address is",i)
print("\nTotal IP address noted is",len(ip_list))



#using regex
import re
ip_search=re.findall("\d{2}.\d{2}.\d{3}.\d{1}",ip)
for i in ip_search:
    print("IP Address is",i)
print("\nTotal IP address noted is",len(ip_search))



#updated program

import re
ip="""IP Address is 10.50.200.1 and also 11.11.500.6 along with 10.50.200.1 also along with 10.50.200.1 also along with 10.50.200.1 along with 10.50.200.1 
    along with 10.50.200.1"""
new_ip = ''.join((i if i in '0123456789.' else ' ') for i in ip)
ip_list=[]
for i in new_ip.split():
    ip_list.append(i)
    
#print(ip_list)
regex_pattern = "^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"

count=0
for i in ip_list:
    result = bool( re.match( regex_pattern,i))
    if (result):
        print("IP Address is:",i)
        count+=1
    #else:
        #print("Invalid")

print("\nTotal IP address noted is",count)
