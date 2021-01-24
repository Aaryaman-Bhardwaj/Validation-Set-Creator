# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:25:33 2021

@author: aaryaman_bhardwaj
"""

import os
import random
import shutil
import pandas as pd
import re

validation_set_size= 5 #in percentage of the training set
data_src="/home/aaryaman_bhardwaj/Documents/ML/yo/" #training set directory from which you want to create the validation set

change_csv= True #true if you want to change the csv file as well
csv_path= "/home/aaryaman_bhardwaj/Documents/ML/yo/train.csv"

    
os.chdir(data_src)

validation_set_names=[]
os.mkdir("validation")

listdir=os.listdir(data_src)
list.sort(listdir)


convert = lambda text: int(text) if text.isdigit() else text.lower()
alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
listdir=sorted(listdir, key=alphanum_key)


for image in listdir:
    if random.randint(0,100) <= validation_set_size:
        shutil.move(image, os.path.join(data_src, "validation"))
        if change_csv:
            validation_set_names.append(image)




if change_csv:
    validation_set_tags=[]
    train_df=pd.read_csv(csv_path)
    for index, row in train_df.iterrows():
        if row['0'] in validation_set_names:
            validation_set_tags.append(train_df._get_value(index,"1"))
    validation_list=list(zip(validation_set_names, validation_set_tags))
    validation_df=pd.DataFrame(validation_list, columns=["0", "1"])
    os.chdir("validation")
    validation_df.to_csv('validation.csv')

print("Validation Set Created")
