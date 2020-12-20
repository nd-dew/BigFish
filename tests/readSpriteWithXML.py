import xml.etree.ElementTree as ET
from pathlib import Path

import pygame

path = Path('../resources/images/sprite_sheets/water_bubbles/water_bubbles.xml')
print(path)
tree = ET.parse(path)
root = tree.getroot()

print(root.tag)
print(root.attrib)

imageName= root.attrib['imagePath']
print(imageName)

water_bubbles_rects_sequence=[]
for child in root:
    rect=[]
    rect.append(child.attrib['x'])
    rect.append(child.attrib['y'])
    rect.append(child.attrib['w'])
    rect.append(child.attrib['h'])
    rect=[int(x) for x in rect]
    print(rect)

imagePath=path.parent / imageName
print(imagePath)
surface = pygame.image.load(imagePath).convert()

# xml.etree.ElementTree

# doc = minidom.parse('../resources/images/sprite_sheets/water_bubbles/water_bubbles.xml')
# TextureAtlas= doc.getElementsByTagName('TextureAtlas')[0]
# print(type(TextureAtlas))
# # print(dir(TextureAtlas))
# print('---------------')
# print(TextureAtlas.Tag)
