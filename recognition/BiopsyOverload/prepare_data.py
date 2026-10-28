import cv2
import os
import math
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt

"""
=========== THE GOAL =============
Prepare the data for the YOLOv7 run
==================================

To accomplish this I need to create the correct data format that yolov7 desires, 
this is:
class x0 y0 x1 y1 x2 y2 ...
Where class is just going to be 0 and indicates lesion
x0, y0 inidicate a vertice on the outline of where the lesion is. 

For each image in the ground truth dataset, load it. 
using csv, identify the corners of the polygon
save them to the .txt file we care about
"""


truthDirectory=Path("/home/groups/comp3710/ISIC2018/ISIC2018_Task1_Training_GroundTruth_x2/")

def main():
    count = 0;
    for image in truthDirectory.iterdir():
        if image.is_file():
            if image.suffix.lower() == ".png":
                count += 1
                img = cv2.imread(image)
                a,b = img.shape[:2]
                corners = cv2.goodFeaturesToTrack(
                    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                    maxCorners=30,
                    qualityLevel=0.01,
                    minDistance=10,
                    blockSize=3,
                    useHarrisDetector=False,
                    k=0.04
                )
                corners = np.intp(corners)  # Convert to integer coords 
                stem = image.stem.replace("_segmentation", "")
                filePath = "processedMasks/" + stem + ".txt"
                with open(filePath, "w", encoding="utf-8") as f:
                    f.write("0 ")
                    for corner in corners:
                        f.write(str(corner[0][0] / a) + " ") 
                        f.write(str(corner[0][1] / b) + " ")
                with open(filePath, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                cleaned_lines = [line.rstrip(" \t") for line in lines]  
                with open(filePath, "w", encoding="utf-8") as f:
                    f.writelines(cleaned_lines) 
    print(f"Done! {count} masks processed")
    return
 
if __name__ == "__main__":
    main()
