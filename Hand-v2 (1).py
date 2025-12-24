import mediapipe as mp
import cv2
import serial
import time
import json


xkyl = 0
xlok = 0
ybpal = 0
xpal = 0
ypal = 0
xzap = 0

k = 0

items = []
palec = {}
kylak = {}
zapiaste = {}
pleco = {}
lokot = {}
bpalc = {}
a = {"palec": palec, "lokot": lokot, "kylak": kylak, "zapiaste": zapiaste, "pleco": pleco}
msg = json.dumps(a)

camera = cv2.VideoCapture(0)

portNo = "/dev/cu.usbmodem14201"
uart = serial.Serial(portNo, 115000)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

mpPose = mp.solutions.pose
pose = mpPose.Pose()


while True:
    xpal = 0
    ypal = 0
    xkyl = 0
    xzap = 0
    xbpal = 0
    ybpal = 0
    xlok = 0
    for ash in range(5):
        star = msg

        if cv2.waitKey(1) == ord('q'):
            exit()

        b = msg
        good, img = camera.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = mpHands.Hands().process(imgRGB)
        palec = {}
        kylak = {}
        zapiaste = {}
        pleco = {}
        lokot = {}
        bpalc = {}

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                for idp, point in enumerate(handLms.landmark):
                    width, height, color = img.shape
                    width, height = int(point.x * height), int(point.y * width)
                    if idp == 12:
                        cv2.circle(img, (width, height), 15, (255, 0, 255), cv2.FILLED)
                        palec = {"x_palec": width, "y_palec": height}
                        xpal += width
                        ypal += height
                    if idp == 9:
                        cv2.circle(img, (width, height), 15, (255, 255, 0), cv2.FILLED)
                        kylak = {"x_kylak": width, "y_kylak": height}
                        xkyl += width
                    if idp == 0:
                        cv2.circle(img, (width, height), 15, (0, 255, 255), cv2.FILLED)
                        zapiaste = {"x_zapieste": width, "y_zapiaste": height}
                        xzap += width
                    if idp == 4:
                        cv2.circle(img, (width, height), 15, (255, 102, 0), cv2.FILLED)
                        bpalc = {"x_bpalc": width, "y_bpalc": height}
                        xbpal += width
                        ybpal += height
        results_p = pose.process(imgRGB)

        if results_p.pose_landmarks:
            mpDraw.draw_landmarks(img, results_p.pose_landmarks, mpPose.POSE_CONNECTIONS)
            for id_p, lm in enumerate(results_p.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id_p == 12:
                    cv2.circle(img, (cx, cy), 15, (11, 102, 35), cv2.FILLED)
                    pleco = {"x_pleco": cx, "y_pleco": cy}
                if id_p == 14:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)
                    lokot = {"x_lokot": cx, "y_lokot": cy}
                    xlok += cx
        a = {"bpalc": bpalc, "kylak": kylak, "lokot": lokot, "zapiaste": zapiaste, "palec": palec, "pleco": pleco}
        if cv2.waitKey(1) == ord('e'):
            palec = {}
            kylak = {}
            zapiaste = {}
            pleco = {}
            lokot = {}
            bpalc = {}
            a = {"bpalc": bpalc, "palec": palec, "kylak": kylak, "lokot": lokot, "zapiaste": zapiaste, "pleco": pleco}
            msg = json.dumps(a)
            s = "000"
            print(s)
            uart.write(s.encode())
            k = 0

        cv2.imshow('Image', img)

    xpal //= 10
    ypal //= 10
    xkyl //= 10
    xzap //= 10
    xbpal //= 10
    ybpal //= 10
    xlok //= 10

    if xkyl < xpal:
        p = '1'
    elif xkyl == xpal or xkyl // 10 == xpal // 10:
        p = "2"
    else:
        p = '0'
    if ybpal > ypal:
        z = "1"
    elif ybpal == ypal or ybpal // 10 == ypal // 10:
        z = "2"
    else:
        z = "0"
    if xzap > xlok:
        m = '1'
        if p == "0":
            p = '1'
        else:
            p = '0'
    elif xzap == xlok or xzap // 10 == xlok //10:
        m = "2"
    else:
        m = '0'
    s = p + z + m + "\n"
    print(s)
    uart.write(s.encode())
