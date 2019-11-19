#https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html

from __future__ import print_function
from datetime import datetime
import cv2 as cv
import argparse
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        #comenta frame para borrar el círculo de la cara
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)
        #print(eyes)
        #mostrar la hora exacta en la que detecta los dos ojos
        if(len(eyes)==2):
            now = datetime.now()
            hora = "{}:{}:{}:{}".format(now.hour, now.minute, now.second, now.microsecond)
            print("Observando",hora)

        #print()
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    cv.imshow('Capture - Face detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
#parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_frontalface_alt.xml')
#parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
#parser.add_argument('--face_cascade', help='Path to face cascade.', default='data\\haarcascade_frontalface_alt.xml')
#parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data\\haarcascade_eye_tree_eyeglasses.xml')
#parser.add_argument('--face_cascade', help='Path to face cascade.', default='C:\\Users\\edduard\\AppData\\Local\\Programs\\Python\\Python35-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_alt.xml')
#parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='C:\\Users\\edduard\\AppData\\Local\\Programs\\Python\\Python35-32\\Lib\\site-packages\\cv2\\data\\haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data\\haarcascade_frontalface_alt.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data\\haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade
face_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
#cap = cv.VideoCapture("video.mp4")
#cap = cv.VideoCapture("video2.mp4")
#cap = cv.VideoCapture("output.avi")
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    #cv.imshow("pantalla",frame)
    #ord("q") para cerrar la pantalla al aplastar la letra q
    #if cv.waitKey(10) == 27:
    if cv.waitKey(10) == ord("q"):
        break