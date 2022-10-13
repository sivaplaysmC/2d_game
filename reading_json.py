import json
import pygame
with open(r"haa.json") as h :
    x = json.load(h)
rect_list = list()
for i in x["rects"] :
    j = pygame.Rect(round( i["x"] ),round(i["y"]),round(i["width"]) , round(i["height"]))
    rect_list.append(j)
