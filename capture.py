import time
import cv2
camera_port = 0
camera = cv2.VideoCapture(0)
time.sleep(0.1)  # If you don't wait, the image will be dark
while True:
	time.sleep(0.40)  # If you don't wait, the image will be dark
	return_value, image = camera.read()
	cv2.imwrite("cam_1.jpg", image)
del(camera)  # so that others can use the camera as soon as possible
