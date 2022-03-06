import cv2
print(cv2.__version__)


camera = cv2.VideoCapture(1)
while True:
    ignore, frame = camera.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("my Webcam", grayFrame)
    cv2.moveWindow('my Webcam', 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
camera.release()