import xml.etree.ElementTree as ET
tree = ET.parse(r'C:\Users\ELCOT\HCL Python Training\john\plant_catalog.xml')
root = tree.getroot()

print("Please Type the preferred plant light exposure level")
print("Available types: Mostly Shady, Mostly Sunny,Sun or Shade,Shade")
aval_type=["Mostly Shady", "Mostly Sunny","Sun or Shade","Shade"]
print()

type_input=input("Enter your types:")
if type_input in aval_type:
    print("You have choosen",type_input,"plant lists!........")
else:
    print("Not available!....")

for i in root.findall('PLANT'):
    com_name=i.find('COMMON').text
    bot_name=i.find("BOTANICAL").text
    zone=i.find("ZONE").text
    light=i.find("LIGHT").text
    price=i.find("PRICE").text
    plant_avail=i.find("AVAILABILITY").text
    if type_input==light:
        print()
        print("Plant Common Name:",com_name)
        print("Plant Price:",price)
        print("Plant availability",plant_avail)