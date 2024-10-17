import cv2

#--How to find the haarcascade_frontalface_default?--
#simply open cmd>>python>>import cv2>>print(cv2.__file__)
#copy that file destination and open the datas folder that contains the haar cascades

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")
#img = cv2.imread("news.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img,
scaleFactor=1.2,
minNeighbors=5)
#print(faces)
#print(type(faces))

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

resized=cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Grey", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
