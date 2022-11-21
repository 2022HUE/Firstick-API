import cv2 as cv
import numpy as np

cap = cv.VideoCapture("src/wood05.mp4")

while True :

    ret, frame = cap.read()
    resize = cv.resize(frame, (0,0), fx = 0.5, fy = 0.5, interpolation = cv.INTER_AREA)

    gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    canny = cv.Canny(blur, 1200, 4000, apertureSize = 5, L2gradient = True)

    # 젓가락 전체
    line = cv.HoughLinesP(canny, 0.2, np.pi / 180 , 50, minLineLength = 300, maxLineGap = 150)

    # 젓가락 전체 출력 / 빨간색
    if line is not None :
        for i in line :
            (a11, b11, a12, b12) = i[0]
            if abs(b11 - b12) < 70 :
                cv.line(resize, (a11, b11), (a12, b12), (0, 0, 255), 2)
                whole = a12 - a11

    cv.imshow("canny_", canny)
    cv.imshow("원본", resize)

    key = cv.waitKey(5)
    if key == 27 :
        break
