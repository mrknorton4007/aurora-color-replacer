#!/usr/bin/env python
import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('_input/Aurora_Skin.xui')
root = tree.getroot()

keyword = ['TextColor', 'Prop', 'FillColor', 'StrokeColor']
tag_list = []
tag_dict = {}

# recursive read child nodes and collect color tags
def recursive_xml_read(node):
    for record in node:
        recursive_xml_read(record)
    if node.tag in keyword and node.text and node.text.startswith('0xff'):
        key = ('<%s>' % node.tag, node.text)
        if key not in tag_list:
            tag_list.append(key)

# start read xml tree
for record in root:
    recursive_xml_read(record)

# order color tags
tag_list.sort()

# convert list to dict
for e in tag_list:
    tag_dict[e] = e[1]

# print the template
print(pprint.pformat(tag_dict))
