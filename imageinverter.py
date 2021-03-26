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

im_size = im.size # size of image in pixels

im = im.convert(mode="RGBA") # removing transparency from any RGBA images by converting them to RGB

pixelmap = np.asarray(im.getdata()) # creating a pixel map of the selected image in an array
                                    # pixelmap = [[R0, G0, B0, A0] [R1, G1, B1, A1]... [Rn-1, Gn-1, Bn-1, An-1]]

pixelmap_copy = np.delete(pixelmap,3,1) # creating a copy of the pixel map without the transparency data 
                                        # pixelmap = [[R0, G0, B0] [R1, G1, B1]... [Rn-1, Gn-1, Bn-1]]

pixelmap_copy = 255 - pixelmap_copy # inverting each colour by subtracting them from 255 (each colour has 1 byte or 8 bits of data)
                                    # pixelmap = [[255-R0, 255-G0, 255-B0] [255-R1, 255-G1, 255-B1]... [255-Rn-1, 255-Gn-1, 255-Bn-1]]

pixelmap[:,0:3] = pixelmap_copy # merging the arrays together so that the editted colour data is replacing the old colour data while maintaining the transparency
                                # pixelmap = [[255-R0, 255-G0, 255-B0, A0] [255-R1, 255-G1, 255-B1, A1]... [255-Rn-1, 255-Gn-1, 255-Bn-1, An-1]]

im.putdata(tuple(map(tuple, pixelmap))) # mapping the 2d array to tuple so the pillow .putdata function can be used

## **IMAGE SAVING** 
selected_image = selected_image.replace(".png","") # removing any labels at the end of the name before saving 
selected_image = selected_image.replace(".jpg","")
selected_image = selected_image.replace(".jpeg","")

im.save(selected_image + "_Inverted.png") # saving inverted image

print(divider, "\nImage has successfully been inverted. A copy of this has been saved in ", currpath)