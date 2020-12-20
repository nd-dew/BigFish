import xml.etree.ElementTree as ET
from pathlib import Path
import pygame


class Sprite():
    def __init__(self, xml_path, initial_position=[0,0]):
        path=Path(xml_path)
        tree = ET.parse(path)
        root = tree.getroot()
        self.spriteCount=0

        imageName = root.attrib['imagePath']
        self.image_path= str(path.parent / imageName)
        self.surface= pygame.image.load(self.image_path).convert_alpha()
        self.surface.set_colorkey([0,0,0])
        self.rects_sequence = []
        self.position=initial_position
        for child in root:
            rect = []
            rect.append(child.attrib['x'])
            rect.append(child.attrib['y'])
            rect.append(child.attrib['w'])
            rect.append(child.attrib['h'])
            rect = [int(x) for x in rect]
            self.rects_sequence.append(rect)

    def blit(self, surface):
        surface.blit(self.surface, self.position,  self.rects_sequence[self.spriteCount])
        self.spriteCount = (self.spriteCount + 1 + len(self.rects_sequence)) % len(self.rects_sequence)
