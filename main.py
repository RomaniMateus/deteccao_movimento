import cv2
import numpy as np

VIDEO = "./videos/Rua.mp4"

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
    ret, frame = cap.read()
    if not ret:
        print("Fim do vídeo")
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("gray_frame", gray_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

cap.release()
