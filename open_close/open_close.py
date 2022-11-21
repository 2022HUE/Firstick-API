import cv2 as cv
import numpy as np

cap = cv.VideoCapture("src/wood05.mp4")

while True :

    ret, frame = cap.read()
    resize = cv.resize(frame, (0,0), fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)

    x = 0; y = 200; w = 1500; h = 500
    roi = resize[y:y+h, x:x+w]

    gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    canny = cv.Canny(blur, 1200, 4000, apertureSize = 5, L2gradient = True)

    # 젓가락 전체
    line = cv.HoughLinesP(canny, 0.2, np.pi / 180 , 50, minLineLength = 300, maxLineGap = 150)

    # 젓가락 전체 출력 / 빨간색
    if line is not None :
        for i in line :
            (a11, b11, a12, b12) = i[0]
            if abs(b11 - b12) < 70 :
                cv.line(roi, (a11, b11), (a12, b12), (0, 0, 255), 2)

            # print(b11, b12)
            
            if (b12 - b11) > 10 :
                print("open")
            else :
                print("close")

    cv.imshow("canny_", canny)
    cv.imshow("원본", resize)
    cv.imshow("roi", roi)

    key = cv.waitKey(50)
    if key == 27 :
        break
