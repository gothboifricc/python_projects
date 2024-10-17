import cv2
lofi = cv2.imread("Lofi.jpg", 0)

print(type(lofi))
print(lofi)
print(lofi.shape)
print(lofi.ndim)

resized_aesthetic = cv2.resize(lofi,(int(lofi.shape[1]/1.2),int(lofi.shape[0]/1.2)))
cv2.imshow("Chill", resized_aesthetic)
cv2.waitKey(0)
cv2.destroyAllWindows()