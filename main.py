import cv2 as cv
import numpy as np

cap = cv.VideoCapture('./assets/images/q1B.mp4')

if (cap.isOpened() == False):
    print('Error opening video file')

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        edges = cv.Canny(frame_gray, 50, 150)

        cnts = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        for c in cnts:
            x, y, w, h = cv.boundingRect(c)
            print(x, y)
            area = w * h
            if area > 100000 and area < 104000:
                rect = cv.rectangle(
                    frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                if (x < 250):
                    cv.putText(frame, 'Passou a barreira', (00, 185), cv.FONT_HERSHEY_SIMPLEX,
                               1, (0, 255, 0), 2, cv.LINE_AA, False)
        cv.imshow('Frame', frame)

        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
