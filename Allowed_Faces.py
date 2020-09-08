'''
@author: Gurpreet Singh
'''

import os
import cv2
import face_recognition
from imutils import paths

def getAllowedFaces():
    curr_dirname = os.getcwd()
    faces_path = os.path.join(curr_dirname, 'Allowed_faces')
    
    allowed_faces = list(paths.list_images(faces_path))
    allowed_faces_encodings = []
    
    
    for face_path in allowed_faces:
        face = cv2.imread(face_path)
        face = face[:, :, ::-1] 
        face_location = face_recognition.face_locations(face)
        curr_encoding = face_recognition.face_encodings(face, face_location)[0]
        
        allowed_faces_encodings.append(curr_encoding)
    
    return allowed_faces_encodings    