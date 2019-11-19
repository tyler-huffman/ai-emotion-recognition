from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os
import numpy as np
import matplotlib.pyplot as plt

#Define the paths to the respective data sets
train_file = r"Data\faceexp-comparison-data-train-public.csv"
test_file  = r"Data\\faceexp-comparison-data-test-public.csv" 

cleanedTrain_file = r"Data\\[Cleaned]TrainData.csv" 

#Reads csv data files
train_data = pd.read_csv(train_file, error_bad_lines=False)
test_data  = pd.read_csv(test_file, error_bad_lines=False)

cleanedTrain_data = pd.read_csv(cleanedTrain_file, error_bad_lines=False)

#Print the size of the data sets by printing the number of rows
#and multiplying the result by 3 as there are 3 images per row
print("Number of Training Images  : {}".format(cleanedTrain_data.shape[0]*3))
print("Number of Validation Images: {}".format(test_data.shape[0]*3))

batch_size = 128
epochs = 15
#Need to determine image height and width


#Downloads Images from csv file
def download_class(c):
    path = 'C:\Users\natet\Documents\GitHub\ai-emotion-recognition'
    dest = path/c
    file = cleanedTrainData
    download_images(path/file, dest, max_pics=2000, timeout=1)
