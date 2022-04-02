import face_recognition
import cv2
import numpy as np
import os
import glob

faces_encodings = []
faces_names = []

cur_direc = os.getcsd()

path = os.path.join(cur_direc, 'data/faces/')

list_of_files = [f for f in glob.glob(path+'*.jpg')]

number_files = len(list_of_files)

names = list_of_files.copy()

for i in range(number_files):
    globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
    globals()['image_encoding_{}'.format(i)] = face_recognition.face_encoding(globals()['image_{}'.format(i)])[0]
    faces_encoding.append(globals()['image_encoding_()'.format(i)])
    
    names[i] = names[i].replace(cur_direc, "")
    faces_names.append(names[i])

                
