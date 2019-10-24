import xml.etree.ElementTree as ET

food_list = []

tree = ET.parse('xml/simple.xml')
menu = tree.getroot()

food_index = -1
for food in menu:
    food_index += 1
    food_list.append({})
    for data in food:
        food_list[food_index][data.tag] = data.text

print(food_list)