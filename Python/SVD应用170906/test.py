import cv2
import numpy as np

img = cv2.imread('yumeko.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def init(image):
    new_image = np.zeros(image.shape,np.uint8)
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            new_image[r,c] = int(image[r,c])
    return new_image

def test(gray_image,n):
    U,s,V = np.linalg.svd(gray_img,full_matrices=False)
    new_image = np.zeros(gray_image.shape)
    print(U.shape,s.shape,V.shape)
    new_s = s[:n]
    new_S = np.zeros((s.shape[0],s.shape[0]))
    new_S[:n,:n] = np.diag(new_s)
    new_image = np.dot(U,np.dot(new_S,V))
    new_image = init(new_image)
    print(new_image)
    return new_image

##cv2.imshow('gray',gray_img)
##list1 = [1,50,100,150,200]
##for n in list1:
##    string = str(round(n*100.0/580,2))+'%'
##
##    cv2.imshow(string,test(gray_img,n))
##
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()

