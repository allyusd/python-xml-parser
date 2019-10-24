import xml.etree.ElementTree as ET

from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, encoding='unicode')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

food_list = []

# Read
tree = ET.parse('xml/simple.xml')
menu = tree.getroot()

food_index = -1
for food in menu:
    food_index += 1
    food_list.append({})
    for data in food:
        food_list[food_index][data.tag] = data.text

print(food_list)

# Write
quick_menu = ET.Element('quick_menu')

for food in food_list:
    item = ET.SubElement(quick_menu, 'item')
    for data in food:
        if data != 'description':
            new_data = ET.SubElement(item, data)
            new_data.text = food[data]

with open("quick_menu.xml", "w") as text_file:
    print(prettify(quick_menu), file=text_file)
