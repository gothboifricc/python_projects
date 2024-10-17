import cv2, time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW) #this parameter signifies the index of the webcam that you have or you can specify the filepath
a=0
while True:
    a=a+1
    check, frame = video.read()

    print(check)
    #check is boolean datatype to check various operations like whether the video is running or not and tells whether its true or false
    print(frame)

    #time.sleep(3)
    cv2.imshow("Capturing", frame)

    key=cv2.waitKey(1)
    #we put the waitKey command before releasing so that after we close the window then it gets released
    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()