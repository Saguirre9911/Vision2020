from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#image = Image.open('File.jpg')
#image.show()
# read the image and define the stepSize and window size 
# (width,height)
image = cv2.imread("8.png") # your image path
size= image.shape
cv2.imshow('image',image)
imgplot=plt.imshow(image)
plt.show()
print(size)
tmp = image # for drawing a rectangle
stepSize = 200
(w_width, w_height) = (200, 200) # window size
for x in range(0, image.shape[1] - w_width , stepSize):
   for y in range(0, image.shape[0] - w_height, stepSize):
      window = image[x:x + w_width, y:y + w_height, :]
      imgplot=plt.imshow(window)
      plt.show()
# classify content of the window with your classifier and  
# determine if the window includes an object (cell) or not
      # draw window on image
      cv2.rectangle(tmp, (x, y), (x + w_width, y + w_height), (255, 0, 0), 2) # draw rectangle on image
      plt.imshow(np.array(tmp).astype('uint8'))
# show all windows
plt.show()