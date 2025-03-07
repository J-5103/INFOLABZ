from PIL import Image,ImageFilter
import numpy as np


#Load an image using Numpy and pillow and convert the image into grayscale Image.


img=Image.open("pexels-anjana-c-169994-674010.jpg")
img.show()

arr_img=np.array(img)
print(arr_img.shape)
print(arr_img)

gray_img=img.convert("L")
print(gray_img)
gray_img.show()


#  FLIP the Image.


flip_img=img.transpose(Image.FLIP_TOP_BOTTOM)##FLIP_LEFT_RIGHT(mirror effect)
print(flip_img)
flip_img.show()


# # Rotate the Image to 110 degrees.

rotate_img=img.rotate(110,expand=True)
print(rotate_img)
rotate_img.show()

# # Save the image to New_image png

img.save("new_image.png",format="png")


# Load an image using NumPy and Pillow

img=Image.open("new_image.png")
img.show()


# Resize the image to 50% of its original dimensions.

width,hieght=img.size

new_size=(width//2,hieght//2)

resized_imag=img.resize(new_size)
print(resized_imag)
resized_imag.show()


# Save the resized image as resized_image.png.

resized_imag.save("resized_image.png")


# # Load an image using NumPy and Pillow
img=Image.open("pexels-photo-6072467.jpeg")
img.show()



# # Flip the image horizontally (left to right).

flipH_img=img.transpose(Image.FLIP_LEFT_RIGHT)##FLIP_LEFT_RIGHT(mirror effect)
print(flipH_img)
flipH_img.show()

# # Flip the image vertically (top to bottom)


flipV_img=img.transpose(Image.FLIP_TOP_BOTTOM)##FLIP_LEFT_RIGHT(mirror effect)
print(flipV_img)
flipV_img.show()

# # Save both flipped images as flipped_horizontal.png and flipped_vertical.png
flipH_img.save("flipped_horizontal.png")
flipV_img.save("flipped_vertical.png")

# Load an image using NumPy and Pillow

img=Image.open("photo-1575936123452-b67c3203c357.jpeg")
img.show()

# Apply a blur effect to the image

blur_img=img.filter(ImageFilter.BLUR)
blur_img.show()

# Save the blurred image as blurred_image.png

blur_img.save("blurred_image.png")
