#---------------------------------------------------Computer Vision-----------------------------------------------------
#Install package Open CV / CV 2
import cv2
import time

#1) Open front camera
#
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     cv2.imshow('Front Camera', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#2) Open front camera in grayscale ( black and white mode )
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow('Front Camera (Grayscale)', gray_frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#3) Change the size of camera screen.
# cap = cv2.VideoCapture(0)
#
# cap.set(3, 640)
# cap.set(4, 480)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     cv2.imshow('Resized Camera', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#4) Create a program that opens camera , captures a photo and saves it and close camera window.
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Failed to capture frame")
#         break
#
#     cv2.imshow('Camera', frame)
#
#
#     if cv2.waitKey(1) & 0xFF == ord('c'):
#         cv2.imwrite('captured_photo.jpg', frame)
#         print("Photo saved as 'captured_photo.jpg'")
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#5) Change the size of captured picture.
#
# cap = cv2.VideoCapture(0)  # Use 1 for front camera, 0 for rear
#
# while True:
#     ret, frame = cap.read()
#
#     cv2.imshow('Camera', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('c'):
#         resized_frame = cv2.resize(frame, (800, 600))
#         cv2.imwrite('resized_photo.jpg', resized_frame)
#         print("Photo saved as 'resized_photo.jpg' with size 800x600")
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#6) Store captured picture in Gray Scale ( black and white mode )

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#
#     cv2.imshow('Camera', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('c'):
#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imwrite('gray_photo.jpg', gray_frame)
#         print("Photo saved as 'gray_photo.jpg' in grayscale")
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#7) Create a program that opens a camera, captures image and stores when user
#press C and close the camera screen when user press E.
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#
#     cv2.imshow('Camera', frame)
#
#     key = cv2.waitKey(1) & 0xFF
#
#     if key == ord('c'):
#         cv2.imwrite('captured_image.jpg', frame)
#         print("Photo saved as 'captured_image.jpg'")
#
#     elif key == ord('e'):
#         print("Exiting...")
#         break
#
# cap.release()
# cv2.destroyAllWindows()

#8) Create a program that opens camera , captures a video for 15 seconds and stores it.
# cap = cv2.VideoCapture(0)
#
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
#
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('captured_video.mp4', fourcc, 20.0, (frame_width, frame_height))
#
# start_time = time.time()
#
# while True:
#     ret, frame = cap.read()
#
#     out.write(frame)
#     cv2.imshow('Recording...', frame)
#
#     if time.time() - start_time >= 15:
#         print("Recording complete. Video saved as 'captured_video.mp4'")
#         break
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("Recording stopped manually. Video saved.")
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()

#9) Create a program that opens a camera, capture videos when user press C , stops
#recording video when user press S.

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = None
recording = False

while True:
    ret, frame = cap.read()
    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c') and not recording:
        out = cv2.VideoWriter('recorded_video.mp4', fourcc, 20.0, (frame_width, frame_height))
        recording = True
        print("Recording started... Press 'S' to stop.")

    if recording:
        out.write(frame)

    if key == ord('s') and recording:
        recording = False
        out.release()
        print("Recording stopped. Video saved as 'recorded_video.mp4'")

    if key == ord('q'):
        if recording:
            out.release()
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()






