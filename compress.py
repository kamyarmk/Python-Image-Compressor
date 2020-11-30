from PIL import Image
import PIL
import os
import glob
import numpy as np

#Gettin All The Images In an Array
images = [file for file in os.listdir() if file.endswith(('jpg', 'png' )) and "Example_" in file]

#Sorting the Array By name
images.sort()

#Flag For Counting
i = 0

#Loop Through Imaged To Compress and Save It
for image in images:
    # 1. Open the image
    img = Image.open(image)
    # 2. Compressing the image
    img.save( str(i) + "_Compressed_and_resized_"+image,
             optimize=True,
             quality=60)
    i += 1


