import cv2
import numpy as np

# read video file
new_capture = cv2.VideoCapture('IGPQ8167.MP4')

# check if the opened successfully
if new_capture.isOpened() == False:
	print("Error for opening the video file")

# Reading the video to complete
while new_capture.isOpened():
	ret, frame = new_capture.read()
	if ret == True:
		cv2.imshow('Frame', frame)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break

# Release when everything is complete
new_capture.release()
# close all frames
cv2.destroyAllWindows()
