import cv2
import sys

VIDEO = "./videos/Ponte.mp4"

algorithm_types = ["KNN", "GMG", "CNT", "MOG", "MOG2"]
algorithm = algorithm_types[0]


def subtractor(algorithm):
    if algorithm == "KNN":
        return cv2.createBackgroundSubtractorKNN()
    elif algorithm == "GMG":
        return cv2.bgsegm.createBackgroundSubtractorGMG()
    elif algorithm == "CNT":
        return cv2.bgsegm.createBackgroundSubtractorCNT()
    elif algorithm == "MOG":
        return cv2.bgsegm.createBackgroundSubtractorMOG()
    elif algorithm == "MOG2":
        return cv2.createBackgroundSubtractorMOG2()
    else:
        print("Algoritmo não encontrado")
        sys.exit(1)


cap = cv2.VideoCapture(VIDEO)
sub = subtractor(algorithm)


def main():

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Fim do vídeo")
            break

        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        mask = sub.apply(frame)

        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    cap.release()


main()
