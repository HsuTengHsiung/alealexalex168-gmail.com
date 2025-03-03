import cv2 
import numpy as np 




img = cv2.imread('../098.picture/ImageCreate.jpg', cv2.IMREAD_UNCHANGED)
 # 設置卷積核 
kernel = np.ones((5, 5), np.uint8) 
dilation = cv2.dilate(img,kernel,iterations = 1) 
cv2.imshow('img', img)
cv2.imshow('dilation', dilation)
cv2.imshow('different', dilation-img)

 
cv2.waitKey(0) 
cv2.destroyAllWindows()
