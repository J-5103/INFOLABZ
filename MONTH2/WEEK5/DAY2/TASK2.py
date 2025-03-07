from PIL import Image
import numpy as np
from numpy import random

img=Image.open("pexels-anjana-c-169994-674010.jpg")
img.show()

#crop the image
# crop_area=(100,100,100,400)

crop_img=img.crop((100,100,100,100))
crop_img.show()

#generate RGBA image

arr_new=random.randint(0,255,(255,255,3),dtype=np.uint8)
print(arr_new)
new_image = Image.fromarray(arr_new)
new_image.show()