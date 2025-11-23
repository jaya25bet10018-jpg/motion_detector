import cv2, time, datetime, imutils


video=cv2.VideoCapture(cv2.CAP_DSHOW)
lst=[]
first_frame=None
a=0
while True:
    a+=1
    frame=video.read()[1]
    text="Unoccupied"
    grayscale_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #to convert the color image to grayscale image....

    gaussian_frame=cv2.GaussianBlur(grayscale_frame,(21,21),0)
    #to convert grayscale image to gaussian blur...

    blur_frame=cv2.blur(gaussian_frame,(5,5))

    if first_frame is None:
        first_frame=grayscale_frame
    else:
        pass
    frame=imutils.resize(frame,width=500) #to resize the frame.!!!!

    frame_delta=cv2.absdiff(first_frame,grayscale_frame) #it gives first_frame pixel diff. between grayscale_frame pixel diff.....

    thresh=cv2.threshold(frame_delta,100,255,cv2.THRESH_BINARY)[1] #to convert the initial image into thresh binary image....

    dialte_image=cv2.dilate(thresh,None,iterations=2)

    cnt=cv2.findContours(dialte_image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #instead of making point side by side it makes two point at the endpoints and join that which saves memory...

    for c in cnt:
        if cv2.contourArea(c)>800:
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            text="Occupied"
        else:
            pass

    font=cv2.FONT_HERSHEY_COMPLEX

    cv2.putText(frame,f"[+] Room Status= {text}",(10,20),font,0.5,(255,0,0),2) #text on frame window...
    lst.append(text+"  "+"at"+" "+str(datetime.datetime.now().strftime("%H:%M:%S")))
    cv2.putText(frame,datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10,frame.shape[0]-10),font,0.35,(0,0,255),1) #date and time

    cv2.imshow("Security feed",frame)
    cv2.imshow("Threshold(foreground mask)",dialte_image)
    #cv2.imshow("Frame delta",frame_delta)

    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        cv2.destroyAllWindows()
        for i in lst:
            print("room was ",i)
        print(a)
        break

