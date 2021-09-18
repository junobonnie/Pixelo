# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:18:50 2020

@author: user
"""

import numpy as np 
import matplotlib.pyplot as plt
import cv2

def img2pixel(inputFile, img_size_ratio, colors = 7):
    img_array = np.fromfile(inputFile, np.uint8)
    imgo = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #imgo = cv2.imread(img)
    #imgo = cv2.fastNlMeansDenoisingColored(imgo,None,25,25,7,21)
    img = cv2.cvtColor(imgo, cv2.COLOR_BGR2LAB)
    #print(img.shape)
    H, W = img.shape[0], img.shape[1]
    img=cv2.resize(img,(int(W*img_size_ratio), int(H*img_size_ratio)),cv2.INTER_CUBIC)
    #plt.imshow(imgo)
    #plt.show()
    Z = img.reshape((-1,3))
     
    # convert to np.float32
    Z = np.float32(Z)
     
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret,label,center=cv2.kmeans(Z,colors,None,criteria,20,cv2.KMEANS_PP_CENTERS)
     
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    res2 = cv2.cvtColor(res2, cv2.COLOR_LAB2RGB)
    
    return res2
    
if __name__ == '__main__':
    #inputFile=r'images/ba.jpg'#'images/ka.jpg'
    inputFile=r'D:\Programing\python_folder\파이썬\duplicate_photo_finder\ax_icon.png'
    result = img2pixel(inputFile,0.1,7)
    plt.imshow(result, interpolation="nearest")
    plt.axis('off')
    plt.show()