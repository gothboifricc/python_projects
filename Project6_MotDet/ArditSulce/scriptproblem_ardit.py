import cv2
#the glob module is used to retrieve files/pathnames matching a specified pattern
import glob

images = glob.glob("*.jpg")

for img in images:
    image = cv2.imread(img, 1)
    resized_image = cv2.resize(image, (100, 100))
    cv2.imshow("Sup", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.imwrite("resized_"+img, resized_image)
