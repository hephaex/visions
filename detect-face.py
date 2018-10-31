import cv2
import matplotlib.pyplot as plt
%matplotlib inline

# image read (imread)
src_image = cv2.imread('lenna.jpeg')
# convert gray 
dst_image = cv2.cvtColor(src_image,cv2.COLOR_RGB2GRAY)
# Haar-like classification
cascade=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
# cascade face detect 
facerect = cascade.detectMultiScale(dst_image, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
# when detect 
if len(facerect) > 0:
    for rect in facerect:
        dst_image = dst_image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
# when not detect
else:
    print("no face")
dst_image = cv2.cvtColor(dst_image,cv2.COLOR_GRAY2RGB)

plt.imshow(dst_image)
