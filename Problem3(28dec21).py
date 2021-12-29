"""
Problem 3: Run length encoding
Run-length encoding is a type of encoding a string.
The basic idea is to represent repeated successive characters as the character of single count.
For example: The string "aaaabbbcccca" would be encoded as a4b3c4a1
"""
input_list=(list(input("Enter the string:")))
input_list.append("")
count=0
output_list=[]
for i in range(len(input_list)):
    try:
        if (input_list[i] in input_list):
            count+=1
        if input_list[i]!=input_list[i+1]:
            output_list.append(str(input_list[i])+str(count))
            count=0
    except IndexError:
        print()
output="".join(output_list)
print("Encoded:",output)