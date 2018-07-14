import cv2
from time import sleep
import numpy

camera = cv2.VideoCapture(0)

while True:
	status, image = camera.read()
	if(status):
		cv2.imwrite("video1.jpg", image)
		
		grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		retval, threshold = cv2.threshold(grayscaled, 60, 255, cv2.THRESH_BINARY)
		
		a = cv2.resize(image, (600, 500))
		cv2.imshow('original',a)
		
		if cv2.waitKey(5) == ord('o'):
			break
		
		b = cv2.resize(threshold, (600, 500))
		cv2.imshow('threshold', b)
		
		if cv2.waitKey(5) == ord('t'):
			break
	sleep(0.03)



