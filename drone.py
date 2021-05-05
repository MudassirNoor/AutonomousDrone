# Team Guardian Autonomy Team
# Spring 2021 Drone
# Computer Vision

import numpy as np
import cv2

# set the stream input
stream = cv2.VideoCapture(0)


def capture(stream):
	# Documentation: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html
	while True:

		# Capture frame
		ret, frame = stream.read()

		# circles_img = images to render the circles  
		# copy the frame and set it to grey scale
		circles_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		# update the frame to greyscale 
		frame = cv2.medianBlur(frame, 5)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT,1, 20, param1=50, param2=30, minRadius=40, maxRadius=50)

		if circles is not None:
			circles = np.uint16(np.around(circles))

			for i in circles[0, :]:
				# draw the outer circle
				cv2.circle(circles_img, (i[0], i[1]), i[2], (0, 255, 0), 2)
				# draw the center of the circle
				cv2.circle(circles_img, (i[0], i[1]), 2, (0, 0, 255), 3)

		cv2.imshow('frame', circles_img)

		# display
		#cv2.imshow('frame', frame)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break	

	# free the stream and window
	stream.release()
	cv2.destroyAllWindows()


def main():
	# retrieve video steam, 0 for webcam ID
	capture(stream)


if __name__ == "__main__":
	main()
