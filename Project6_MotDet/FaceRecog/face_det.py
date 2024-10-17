import numpy as np
import cv2, time, pandas
from datetime import datetime

status_list = [None, None]
times = []
df = pandas.DataFrame(columns = ["Start", "End"])

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while(True):
    status = 0
    #Capture frame by frame
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)
    for (x, y, w, h) in faces:
        status = 1
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #y_cord start:y_cord end, x_cord start:x_cord end
        roi_color = frame[y:y+h, x:x+h]
        
        
        #Recognize? Deep learned model predict keras tensorflow pytorch scikit-learn

        #img_item = "my-image.png"
        #cv2.imwrite(img_item, roi_gray)

        color = (255, 0, 0) #BGR 0-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        cv2.putText(frame, "Status: {}".format('Detected'), (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 255, 0), 2)
    status_list.append(status)
    #status_list = status_list[-2:]    
    
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
    if status == 0:
        cv2.putText(frame, "Status: {}".format('Welcome'), (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 0, 255), 2)
    #else:
        #df = df.append({"CurStat": "Movement Detected"}, ignore_index = True)  #CORRECTION REQUIRED
    #Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        if status == 1:
            times.append(datetime.now())
        if len(times) % 2 != 0:                 # check if "times" list is odd
            del times[0]
        break
print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index = True)

df.to_csv("Times.csv")

cap.release()
cv2.destroyAllWindows()