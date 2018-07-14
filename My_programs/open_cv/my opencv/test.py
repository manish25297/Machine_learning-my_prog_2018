import cv2
import numpy as np

cap=cv2.VideoCapture(0)
b=cv2.VideoWriter_fourcc(*'XVID')
c=cv2.VideoWriter('output.avi',b,5.0,(640,480))

while True:
    status,image=cap.read()
    image=cv2.flip(image,1)
    cv2.imshow("image",image)
    c.write(image)
    
    s=cv2.waitKey(100)
    if s==ord("q"):
        break

cap.release()
c.release()
cv2.destroyAllWindows()
