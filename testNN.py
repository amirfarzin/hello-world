# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 01:13:14 2018

@author: amir farzin
"""

    
import mnist_loader
import MyNetwork
import numpy as np
import timeit

#training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net=MyNetwork.Network([784,30,10])

start=timeit.default_timer() 
net.SGD(training_data,30,10,0.5,evaluation_data=test_data,monitor_evaluation_accuracy=True)
stop=timeit.default_timer()
print time.strftime('total time : %H:%M:%S', time.gmtime(stop-start))

#print training_data[1][1]






"""
from PIL import Image

img = Image.new( 'L', (28,28), "white") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = a[j][i]*255
        print a[i][j]# set the colour accordingly
img=img.resize((250,250))
img.show()"""
