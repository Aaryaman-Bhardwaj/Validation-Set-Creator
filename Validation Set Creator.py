# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:25:33 2021

@author: aaryaman_bhardwaj
"""

import os
import random
import shutil

validation_set_size= 5 #in percentage of the training set
data_src="/home/aaryaman_bhardwaj/Documents/ML/yo/" #training set directory from which you want to create the validation set

os.chdir(data_src)

validation_set_list=[]
os.mkdir("validation")

for image in os.listdir(data_src):
    if random.randint(0,100) <= validation_set_size:
        shutil.move(image, os.path.join(data_src, "validation"))

print("Validation Set Created")