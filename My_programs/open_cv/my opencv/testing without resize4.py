import cv2
import numpy as np

a=cv2.VideoCapture(0)

while(True):
    status,im=a.read()
    cv2.imshow("testing cv2 without resize",im)

    k= cv2.waitKey(1)   #never put zero here otherwise the screen is not going to
                         #to be refresh and you will see a stable image
    if k==ord("q"):
        break
a.release()
cv2.destroyAllWindows()


