import cv2, time
# VIDEO_FILENAME = "capture.mp4"

first_frame = None

video = cv2.VideoCapture(0)

while True:
  check, frame = video.read()

  cv2.imshow("Capturing", frame)

  key = cv2.waitKey(1000)

  if key == ord('q'):
    break


video.release()
cv2.destroyAllWindows()