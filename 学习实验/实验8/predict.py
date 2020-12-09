# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 12:04
# @FileName: predict.py
# @Author  : CNPolaris
import os
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img
import matplotlib.pyplot as plt

label = np.array(['cat', 'dog'])
model = load_model('model.h5')
path = 'image/test'
files = os.listdir(r'image/test')
for filepath, dirnames, filenames in os.walk(r'image/test'):
    print(filepath)
    for file in filenames:
        image_path = filepath + '\\' + file
        image = load_img(image_path)
        image = image.resize((150, 150))
        temp = image
        image = img_to_array(image)
        image = image / 255
        image = np.expand_dims(image, 0)
        # print(image.shape)
        result = label[model.predict_classes(image)]
        print(image_path+" label is predicted  "+result[0][0])
        if result[0][0] == 'cat':
            plt.imsave('image/validation/cats/' + file, temp)
        elif result[0][0] == 'dog':
            plt.imsave('image/validation/dogs/' + file, temp)
