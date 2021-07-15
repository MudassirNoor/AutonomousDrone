# Team Guardian Autonomy Team
# Spring 2021 Drone NEW
# Computer Vision
# Ref: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_houghcircles/py_houghcircles.html

import numpy as np
import cv2

# set the stream input
# TODO: change to ESP-32 camera stream 
stream = cv2.VideoCapture(0)
	


def capture(stream):

	while True:
		# Capture frame
		ret, frame = stream.read()

		# circles_img = images to render the circles
		circles_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		# update the frame to greyscale 
		frame = cv2.medianBlur(frame, 5)
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# TODO: parameters require adjusting to reduce false detection
		# TODO: switch to blob detection
		circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=40, maxRadius=50)

		if circles is not None:
			circles = np.uint16(np.around(circles))

			for i in circles[0, :]:
				coordString = str(i[0]) + ',' + str(i[1]) # circle coordinate
				print("Detecting circle at: " + coordString)

				# setup the circle parameters
				circleCoords = (i[0], i[1]) 
				circleRadius = i[2]
				circleColor = (0, 255, 0)
				circleBorder = 2 

				cv2.circle(circles_img, circleCoords, circleRadius, circleColor, circleBorder)

				# setup the text parameters
				textCoords = (i[0] - 30, i[1])
				textFont = cv2.FONT_HERSHEY_SIMPLEX
				textSize = 0.5
				textColor = (0, 255, 0)
				textThickness = 1
		
				cv2.putText(circles_img, coordString, textCoords, textFont, textSize, textColor, textThickness)

		# display the frame with circles drawn 
		cv2.imshow('frame', circles_img)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break	

	stream.release()
	cv2.destroyAllWindows()


def main():
	capture(stream)


if __name__ == "__main__":
	main()
