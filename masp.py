import multiprocessing as mp 
import cv2
import numpy as np
import time

width = 640
height = 480
    

def foo( child ):
    return

def make_capture():
    # open webcam video stream
    cap = cv2.VideoCapture(0)
    return cap

def video_in( parent ):
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = make_capture()
    cv2.startWindowThread()

    while( True ):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # resizing for faster detection
        frame = cv2.resize(frame, (width, height))
        if frame is not None:
            parent.send(frame_calc(frame, face_cascade))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    # When everything done, release the capture
    cap.release()
    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)




def frame_calc(frame, face_cascade):
    # detect people in the image
    # returns the bounding boxes for the detected objects
    # boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )
    
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    
    boxes = face_cascade.detectMultiScale(gray,
    minSize=(70, 70),  minNeighbors=10)

    
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    
    cv2.imshow('frame', frame)    
    new_x_offset = 0
    x_offset = 0
    
    if(len(boxes) > 0):
        for box in boxes:
            new_x_offset += (box[0] + box[2]) / 2
        new_x_offset = new_x_offset / len(boxes)
        if(new_x_offset > width / 2):
            x_offset = -1
        else:
            x_offset = 1
    
    return x_offset


if __name__ == '__main__':    
    parent, child = mp.Pipe()

    video_in_p = mp.Process(target=video_in, args=(parent, ))
    direction_p = mp.Process(target=foo, args=(child,))


    video_in_p.start()
    direction_p.start()

    while (True):
        print(child.recv())
