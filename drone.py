# Team Guardian Autonomy Team
# Spring 2021 Drone
# Computer Vision

import numpy
import cv2


def capture(stream):
    while True:

        # Capture frame
        ret, frame = stream.read()

        # display
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # free the stream and window
    stream.release()
    cv2.destroyAllWindows()


def main():
    # retrieve video steam, 0 for webcam ID
    capture(stream=cv2.VideoCapture(0))


if __name__ == "__main__":
    main()
