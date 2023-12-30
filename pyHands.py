import cv2
import mediapipe


camera = cv2.VideoCapture(0)

while True:
    _, img = camera.read()

    cv2.imshow("User image", img)

    if cv2.waitKey(20) & 0xFF==ord('q'):      # --waitKey(20)-- está esperando o parâmetro "q"(20), base documentação OpenCV. --0xFF==ord('q')-- Máscara para ler apenas os primeiros 8 bits, e se representa a letra "q".
        break