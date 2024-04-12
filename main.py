import cv2
import numpy as np
from time import sleep

VIDEO = "./videos/Rua.mp4"
delay = 10

cap = cv2.VideoCapture(VIDEO)
_, frame = cap.read()

frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)

frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)
print(medianFrame)

cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
gray_median_frame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray_median_frame", gray_median_frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

while True:
    tempo = float(1 / delay)
    sleep(tempo)

    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo")
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray_frame, gray_median_frame)
    _, diff = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("diff", diff)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
