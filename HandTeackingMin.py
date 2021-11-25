import cv2
import numpy as mp 
import time
import push_up as htm

######################
wCam, hCam = 640, 480
######################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)


    cTime = time.time()
    fps =  1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}',(40,70), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()