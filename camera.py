import cv2
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
