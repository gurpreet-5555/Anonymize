'''
@author: Gurpreet Singh
'''

import face_recognition
import os
from imutils import paths
import numpy as np
import cv2
import datetime


def blur(input_image, allowed_faces_encodings, upsample):
    
    start = datetime.datetime.now()
    input_image = input_image[:, :, ::-1]   # BGR to RGB
    detected_faces = face_recognition.face_locations(input_image, number_of_times_to_upsample=upsample)
    detected_encodings = face_recognition.face_encodings(input_image, detected_faces)
    blur_regions = []
    end = datetime.datetime.now()
    
    for i, encoding in enumerate(detected_encodings):
        
        matches = face_recognition.compare_faces(allowed_faces_encodings, encoding)
        face_distances = face_recognition.face_distance(allowed_faces_encodings, encoding)
        
        if len(matches) ==0:
            blur_regions.append(detected_faces[i])
            continue
        
        best_match_index = np.argmin(face_distances)
        #print(best_match_index)
        if not matches[best_match_index]:
            blur_regions.append(detected_faces[i])

    return blur_regions                   
