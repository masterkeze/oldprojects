import cv2
import numpy as np

img = np.zeros((200,200),dtype = np.uint8)
print(img.shape)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
