import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
camobj = cv2.VideoCapture(0, cv2.CAP_DSHOW) 


def main():

    #check if camera opened
    if not camobj.isOpened():
        print("Camera not accessible")
        return


    while True:
        ret, frame = camobj.read()
        if not ret:
            break
        
        small = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)



        #gray scale
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        #Face detection
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize = (60,60))


        

        for (x, y, w, h) in faces:
            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)


            #Rectangle drawing
            cv2.rectangle(frame, (2*x, 2*y), (2*(x + w), 2*(y + h)), (150, 150, 150), 2)

        
        

        output = cv2.resize(frame, (1200, 900))

        # Display the resulting frame
        cv2.imshow("blah", output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camobj.release()
    cv2.destroyAllWindows()



main()