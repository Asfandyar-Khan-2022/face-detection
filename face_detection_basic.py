import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('videos/video7.mp4')
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.7)

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img,detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img,f'detection_percentage: {int(detection.score[0]*100)}', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN,
                        5,(255, 0, 255), 5)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img,f'FPS: {int(fps)}', (20,200), cv2.FONT_HERSHEY_PLAIN,
                10,(0, 255, 0), 5)
    
    cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('custom window', img)
    key = cv2.waitKey(10)
    if key > 0:
        break