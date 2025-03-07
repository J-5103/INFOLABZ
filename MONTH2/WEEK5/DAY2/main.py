

from numpy import random
from PIL import Image
import numpy as np


img=Image.open("pexels-anjana-c-169994-674010.jpg")
# img.show()
#
# arr_img=np.array(img)
# print(arr_img.shape)
# print(arr_img)
#
# arr_new=random.randint(0,255,(255,255,3),dtype=np.uint8)
# print(arr_new)
# new_image = Image.fromarray(arr_new)
# new_image.save("image.png")

# generate red imag
#
# hieght=100
# width=100
#
# red_canvas=np.full((hieght,width,3),(255,0,0),dtype=np.uint8)
# print(red_canvas)
# red_img=Image.fromarray(red_canvas)
# red_img.save("red.png")

#GREEN canvas
# hieght=100
# width=100
#
# green_canvas=np.full((hieght,width,3),(0,255,0),dtype=np.uint8)
# print(green_canvas)
# green_img=Image.fromarray(green_canvas)
# green_img.save("green.png")
#

#BLUE canvas
# hieght=100
# width=100
#
# blue_canvas=np.full((hieght,width,3),(0,0,255),dtype=np.uint8)
# print(blue_canvas)
# blue_img=Image.fromarray(blue_canvas)
# blue_img.save("blue.png")
#

#white canvas
#
# hieght=100
# width=100
#
# white_canvas=np.full((hieght,width,3),(255,255,255),dtype=np.uint8)
# print(white_canvas)
# white_img=Image.fromarray(white_canvas)
# white_img.save("white.png")

#black canvas

hieght=100
width=100

black_canvas=np.full((hieght,width,3),(0,0,0),dtype=np.uint8)
print(black_canvas)
black_img=Image.fromarray(black_canvas)
black_img.save("black.png")


