import cv2
import numpy as np



a=cv2.VideoCapture(0)

while (True):
    
    
   
    status,img=a.read()
    img1=img
    k=0
    while(k<3):
        j=0
        while(j<400):
            i=0
            while(i<400):
                img1[i][j][k] = 255-img[i][j][k]
                i=i+1
            j=j+1
        k=k+1      
        
    
            
    
  
    
    cv2.imshow("camera",img1)
    if cv2.waitKey(12)==ord('q'):
        break
    

a.release()
cv2.destroyAllWindows()
