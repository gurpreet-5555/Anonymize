'''
@author: Gurpreet Singh
'''

import cv2
import face_recognition
import datetime
from Face_Matching import blur
from Allowed_Faces import getAllowedFaces
import os
import argparse
from os import system, name

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--stream", help="Video stream source")
parser.add_argument("-u","--upsample", type=int , default=1 , help="Scale to upsample the image for better face detection. Note: Higher upsample reduces speed. Default value = 1")
parser.add_argument("-d", "--display", type=bool, default=False, help="True: Display frames while rendering input video stream. Default value = False")
parser.add_argument("-o", "--output", required=True, help="Path to output directory")
args = vars(parser.parse_args())

no_of_frames = 0
current_frame = 0
flip = False

if args["stream"] in ['0','1','2','3','4','5']:
    stream = cv2.VideoCapture(int(args["stream"]))
    flip = True
else:
    stream = cv2.VideoCapture(args["stream"])
    no_of_frames = int(stream. get(cv2.CAP_PROP_FRAME_COUNT))
    
    
allowed_faces = getAllowedFaces()

curr_dirname = os.getcwd()

if args["output"] is None:
    out_path = os.path.join(curr_dirname, 'Output\\')
else:
    out_path = args["output"]
    
writer = None

while True:
    start = datetime.datetime.now()
    isRead, frame = stream.read()
    if not isRead:
        break
    
    if flip:
        frame = cv2.flip(frame, 1)
        
    clone = frame.copy()
    current_frame += 1
       
    scale_down = 0.4
    scale_up = 1/scale_down
    frame = cv2.resize(frame, (int(frame.shape[1]*scale_down),int(frame.shape[0]*scale_down)))
    face_locations = []
    blur_regions = blur(frame, allowed_faces, int(args["upsample"]))
    if len(blur_regions) > 0:
        for region in blur_regions:
            (top, right, bottom, left) = region
            text = ""    
            roi = clone[int(top*scale_up):int(bottom*scale_up) , int(left*scale_up):int(right*scale_up)]
            blurred_face = cv2.GaussianBlur(roi, (51,51), 0)
            clone[int(top*scale_up):int(bottom*scale_up) , int(left*scale_up):int(right*scale_up)] = blurred_face
    
    end = datetime.datetime.now()

    if args["display"]:
        cv2.imshow('Stream', clone)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
    (H,W) = clone.shape[:2]
    if writer is None:
        writer = cv2.VideoWriter(out_path+'\\output.avi', cv2.VideoWriter_fourcc(*'mp4v'), stream.get(cv2.CAP_PROP_FPS) , (W,H), True)
    
    writer.write(clone)  
    
    # Clear Windows Console   
    if name == 'nt': 
        system('cls') 
  
    # Clear Linux, MacOS console
    else: 
        system('clear') 
        
    print("{} % complete".format(round((current_frame/no_of_frames)*100), 2))

writer.release()
stream.release()    
    