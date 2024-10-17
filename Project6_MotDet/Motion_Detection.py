import cv2


first_frame=None # Assign the none value so that it is defined


video=cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    check, frame = video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(5,5),0)

    if first_frame is None:
        first_frame=gray
        continue #continue command says that proceed to the beginning of the while loop because we don't want it to run the below commands for now but on the next iteration
    
    delta_frame=cv2.absdiff(first_frame,gray)
    _, thresh_frame=cv2.threshold(delta_frame, 20, 255, cv2.THRESH_BINARY)
    dilated =cv2.dilate(thresh_frame, None, iterations=3)

    contours, _ =cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 200:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Thresh Frame", thresh_frame)
    cv2.imshow("Colour Frame", frame)

    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame)
    
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()