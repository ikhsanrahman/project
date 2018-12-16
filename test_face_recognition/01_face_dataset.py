import cv2
import numpy

cam=cv2.VideoCapture(0)
#set width and height of display
cam.set(6,840)
cam.set(10,480)
#define and import file which describe face recognition
face_detector=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#first step to take photograph
face_id=input('\n enter user id and press ==>')
print ("\n [INFO] Initializing Face capture of user. Look at the camera, focus, don't move and wait... ")
#Initialize individual sampling face count
count =0
while True:
    ret, img=cam.read()
    img=cv2.flip(img, 1) #open camera and get the picture horizontally
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #change the image grom BGR to gray
    face_detect=face_detector.detectMultiScale(gray, 1.3, 3) #this means that detects image that has been changed to gray
    for (x,y,w,h) in face_detect:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)


    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    elif count ==30:
        break
print ("\n [INFO] Exiting Program and Clean Up Stuff")
cam.release()
cv2.destroyAllWindows()
