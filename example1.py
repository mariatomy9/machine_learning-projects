import cv2

cap = cv2.VideoCapture(0)  # webcam

while cap.isOpened():
    # Simply reading the picture
    ret, back = cap.read()
    if ret:
        # back is what camera is reading
        cv2.imshow('image', back)
        if cv2.waitKey(5) == ord('q'):
            # save the image
            cv2.imwrite('E:/image2.jpg', back)
            break
cap.release()
cap.destroyAllWindows()
