
import cv2
import os
#1. Open the front camera in normal mode. Allow the user to press 'S' to capture a
#selfie, but store the image in grayscale.
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret,frame=cap.read()
#     cv2.imshow("press s to capture",frame)
#
#     key = cv2.waitKey(1) & 0xFF
#     if key == ord('s'):
#         cv2.imwrite("selfie_grayscale.jpg",cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY))
#         print("saved as selfie_grayscale.jpg")
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#2. Open the front camera in a mirrored mode
#
# cap=cv2.VideoCapture(0)
#
# while True:
#     ret,frame=cap.read()
#     frame=cv2.flip(frame,1)
#     cv2.imshow("press q to exit",frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#3. Open the front camera with a frame displaying your name in the frame.
#
# cap=cv2.VideoCapture(0)
#
# while True:
#     ret,frame=cap.read()
#     frame=cv2.flip(frame,1)
#
#     cv2.putText(frame,"Jimi Patel",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
#
#     cv2.imshow("press q to exit",frame)
#
#     if cv2.waitKey(1) & 0xFF==ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#4. Create an image filter program that:
#○ Loads an image from the input_images folder.
#○ Applies three filters:
# ■ Gaussian Blur (7x7)
# ■ Median Blur (5)
# ■ Bilateral Filter (9, 75, 75)
#○ Saves all three processed images in the filtered_images folder.

img = cv2.imread("Input_image/ganpati.jpg")

cv2.imwrite("filtered_images/gusssian.jpg",cv2.GaussianBlur(img,(7,7),3))
cv2.imwrite("filtered_images/meadin.jpg",cv2.medianBlur(img,17))
cv2.imwrite("filtered_images/bilateral.jpg",cv2.bilateralFilter(img,5,25,25))

print("filter applied and image saved")


#5. Allow the user to enter the height and width of an image. Resize the image
#accordingly and store it in a folder called output_images.
# img=cv2.imread("Input_image/ganpati.jpg")
#
# if img is None:
#     print("Error: Image not found or invalid image path!")
#     exit()
# width=int(input("enter image width:"))
# height=int(input("enter image height:"))
#
# resized=cv2.resize(img,(width,height))
#
# os.makedirs("output_images",exist_ok=True)
#
# cv2.imwrite("output_images/resized.jpg",resized)
#
# print("image resized and saved successfully")

#6. Store 10 images in the input_images folder. Load all images using a loop or any
#other logic, convert them to grayscale, and store them in the gray_images folder.
#
# input_folder="Input_image"
# output_folder="gray_images"
#
# os.makedirs(output_folder,exist_ok=True)
# for filename in os.listdir(input_folder):
#     img_path=os.path.join(input_folder,filename)
#
#     img=cv2.imread(img_path)
#
#     gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
#     gray_path=os.path.join(output_folder,filename)
#     cv2.imwrite(gray_path,gray_img)
#
#     print(f"processed:{filename}")
#
# print("all images converted and saved")

#7. Load Image from folder and detect edges of the image and store it as edge_image in folder.

# img=cv2.imread("Input_image/girl.jpg", cv2.IMREAD_GRAYSCALE)
#
# edges=cv2.Canny(img,100,600)
#
# os.makedirs("edge_image", exist_ok=True)
#
# cv2.imwrite("edge_image/edge.jpg", edges)
#
# print("edge image saved successfully")


