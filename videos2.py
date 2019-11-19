#https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('video.mp4')
#cap = cv.VideoCapture('output.avi')
contador = 0
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #gray = cv.flip(frame,1)    #giro del video(no se queda con el color gray)
    #cv.imshow('Pantalla 1', frame)
    cv.imshow("Pantalla 2",gray)
    contador+=1
    print(contador)
    #subir el valor de waitKey para que se muestre el video más despacio
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()