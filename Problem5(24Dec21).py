#Problem 5
"""
Display interactive menu to select the food names.
Once name is obtained, list the price, description and calories of the food item and prompt a question regarding the number of items for order
Once order count is obtained, display order placed for item xxx and total cost of the order is $______
"""
import xml.etree.ElementTree as ET
from itertools import repeat

tree = ET.parse(r'C:\Users\ELCOT\HCL Python Training\john\food.xml')
root = tree.getroot()

#available food list
food_list=[]
print("Available foods list:")
for i in root.findall("food"):
    food_name=i.find("name").text
    print(food_name)
    food_list.append(food_name)


#input food
print()
user_food=input("Enter the food name:")
if user_food in food_list:
    print("You have choosen:",user_food)
else:
    print("Not available!....")

#details of chosen food
for i in root.findall("food"):
    food_name=i.find("name").text
    food_price=i.find("price").text
    food_des=i.find("description").text
    food_cal=i.find("calories").text
    if user_food==food_name:
        print()
        print("food name:",food_name)
        print("Price:",food_price)
        print("Decription:",food_des)
        print("Calories:",food_cal)
        print()
        order=int(input("Number items for the order:"))
        m=float(food_price[1:])
        n=[]
        n.extend(repeat(m,order))
        print()
        print("your order is place!...")
        print()
        print("Order details:")
        print("Food Item:",food_name)
        print("total cost of the order:$",round(sum(n),2))
