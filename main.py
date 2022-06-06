import cv2 as cv
import numpy as np

cap = cv.VideoCapture('./assets/images/q1A.mp4')

if (cap.isOpened() == False):
    print('Error opening video file')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        upper_red = np.array([180, 255, 255])
        lower_red = np.array([160, 50, 50])
        mask_red1 = cv.inRange(frame_hsv, lower_red, upper_red)

        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask_red2 = cv.inRange(frame_hsv, lower_red, upper_red)

        upper_blue = np.array([135, 255, 255])
        lower_blue = np.array([90, 50, 50])
        maskblue = cv.inRange(frame_hsv, lower_blue, upper_blue)

        mask_red = mask_red1 + mask_red2

        cnts = cv.findContours(mask_red, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for c in cnts:
            x, y, w, h = cv.boundingRect(c)
            area = w * h
            rect = cv.rectangle(
                frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv.imshow('Frame', frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
