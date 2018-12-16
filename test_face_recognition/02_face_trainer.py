import cv2
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import os
path='dataset'
data=[]
for images in os.listdir(path):
    img=cv2.imread(images)
    data.append(img)

data1=np.array (data)

names=['ikhsan']

count=0
name=[]
while count<30:
    for x in names:
        name.append(x)
    count+=1

print(len(name))
