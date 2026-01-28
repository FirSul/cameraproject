import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
camobj = cv2.VideoCapture(0, cv2.CAP_DSHOW) 


def main():


    if not camobj.isOpened():
        print("Camera not accessible")
        return

    while True:
        ret, frame = camobj.read()
        if not ret:
            break
        

        cv2.rectangle(frame, (0,0), (640, 480), (0, 255, 0), 2)
        cv2.imshow("blah", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camobj.release()
    cv2.destroyAllWindows()



main()