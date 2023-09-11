import cv2
import numpy as np
# reading and writing in files

# img = cv2.imread('lena.jpg',1)
img= np.zeros([512,512,3],np.uint8)
img = cv2.line(img, (0,0),(255,255),(255,0,0),2)
img = cv2.arrowedLine(img, (0,255),(255,255),(255,0,0),2)

img = cv2.rectangle(img, (384,0),(510,128),(0,0,255),2)
img=cv2.circle(img, (447,63),63,(0,255,0),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img, 'OpenCV',(10,500),font,4,(255,255,255),10,cv2.LINE_AA)
# display
cv2.imshow('image',img)

k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()