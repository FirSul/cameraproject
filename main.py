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





    #tracker initiliaztion
    tracker = None
    bbox2 = None
    

    while True:
        ret, frame = camobj.read()
        if not ret:
            break
        




        if tracker is None:
            #grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize = (60,60))
            if len(faces) > 0:
                (x, y, w, h) = faces[0]
                tracker = cv2.TrackerCSRT_create()
                tracker.init(frame, (x, y, w, h))
                bbox2 = (x, y, w, h)
                
        else:
            success, bbox = tracker.update(frame)
            if success:
                (x,y,w,h) = map(int, bbox)
                bbox2 = (x, y, w, h)
            else:
                tracker = None
            
            if bbox2 is not None:
                (x, y, w, h) = bbox2
                cv2.rectangle(frame, (x, y), (x + w, y + h), (100, 100, 100), 2)















        
        
        

        output = cv2.resize(frame, (1000, 800))


        # Display the resulting frame
        cv2.imshow("blah", output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camobj.release()
    cv2.destroyAllWindows()



main()