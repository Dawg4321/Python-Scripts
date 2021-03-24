# image_Inverter
# This is a simple application which will invert the colours in any png and jpg image.

from PIL import Image
import numpy as np
import os


currpath = os.path.dirname(os.path.abspath(__file__)) # locating current path of python file
divider = "~~~~~~~~~~~~~~~~~~~~~~"

# **MAIN MENU**
print("\nWelcome to the Image Inverter\n",divider, "\nPlease move an Image into the directory:", currpath,"\n", divider)
input("Press enter to continue")

files = os.listdir(currpath) #locating all files in current directory
images = [] # list for storing located images

print("Please select an image to invert :")

for f in range(len(files)):  # printing all of the images for user to view
    if ".png" in files[f] or ".jpeg" in files[f] or ".jpg" in files[f]:    # system can be tricked in file contains.png, .jpg or .jpeg in name
        images.append(files[f]) # storing all found images in the images array 
        print(len(images),".",files[f])

## **IMAGE SELECTION**
print(divider)
selected_image = input("Enter a value from 1 - " + str(len(images))+": ") 
print(divider, "\nInverting Image...")

selected_image = images[int(selected_image) - 1] # locating the selected image in the images list

## **IMAGE INVERSION**
im = Image.open(selected_image) # opening the image for processing
im = im.convert(mode="RGB") # removing transparency from any RGBA images by converting them to RGB

pixelmap = np.asarray(im) # creating a pixel map of the selected image in an array [R0, G0, B0, R1, G1, B1... Rn-1, Gn-1, Bn-1]

pixelmap = 255 - pixelmap # inverting each colour by subtracting them from 255 (each colour has 1 byte or 8 bits of data)

im = Image.fromarray(pixelmap) # creating new image with modified pixel map

im.show() # displaying inverted image

## **IMAGE SAVING** 
selected_image = selected_image.replace(".png","") # removing any labels at the end of the name before saving 
selected_image = selected_image.replace(".jpg","")
selected_image = selected_image.replace(".jpeg","")

im.save(selected_image + "_Inverted.png") # saving inverted image

print(divider, "\nImage has successfully been inverted. A copy of this has been saved in ", currpath)