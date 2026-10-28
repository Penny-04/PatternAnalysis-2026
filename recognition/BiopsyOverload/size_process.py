import cv2
import os
import math
from pathlib import Path

directory=Path("/home/groups/comp3710/ISIC2018/ISIC2018_Task1-2_Training_Input_x2/")

largestX = 0
largestY = 0
smallestX = float("inf")
smallestY = float("inf")

paths = ["", "", "", ""]

for image in directory.iterdir():
    if image.is_file():
        if image.suffix.lower() == ".png" or image.suffix.lower() == ".jpg":
            img = cv2.imread(image)
            a,b = img.shape[:2] 
            if a > largestX:
                largestX = a
                paths[0] = image;
            if a < smallestX:
                smallestX = a
                paths[1] = image;
            if b > largestY:
                largestY = b
                paths[2] = image;
            if b < smallestY:
                smallestY = b
                paths[3] = image;
            

print("LargestX =", largestX, " largestY =", largestY, "SmallestX =", smallestX, "SmallestY =", smallestY)
print("Path Large X=", paths[0], "largeY =", paths[1], "SmallX=", paths[2], "SmallY =", paths[3])
