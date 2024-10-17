import cv2, time
from datetime import datetime
import numpy as np

status_list = [None, None]
times = []

video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret, frame1 = video.read()
ret, frame2 = video.read()

while True:
    status = 0
    diff =cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0) 
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ =cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 10), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 0, 255), 3)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    cv2.imshow("Feed", frame1)
    frame1 = frame2
    ret, frame2 = video.read()

    key=cv2.waitKey(1)
    if key==ord('q'):
        if status==1:
            status_list.append(datetime.now())
        break
    
    print(status_list)
    print(times)
video.release()
cv2.destroyAllWindows()