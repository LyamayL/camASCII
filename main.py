import cv2 as cv
import numpy as np

WIDTH = 100
chars = "@%#*+=-:. "

def convert_frame(frame):
    # On calcule le ratio de l'image (*.5 car un pixel est 2 fois plus haut que large dans le terminal)
    HEIGHT = int(WIDTH * (frame.shape[0] / frame.shape[1]) * 0.5)
    frame = cv.resize(frame, (WIDTH, HEIGHT))

    # Frame de type np.array()
    # On calcule le niveau de gris sur tous les px d'un coup grace au vectoring
    G = (frame[:, :, 0] + frame[:, :, 1] + frame[:, :, 2])/3
    C = G * ((len(chars) - 1)/255)

    to_print = ""
    for line in range(len(C)):
        for x in range(len(C[0])):
            b, g, r = frame[line, x]

            char = chars[int(C[line, x])]

            # 38 = chgt de couleur et 2 pour dire que c'est du rgb. Le m est un délimiteur
            to_print += f"\033[38;2;{r};{g};{b}m{char}"

            
            
        to_print += "\n"

    return to_print
    



# Ouvrir la cam
capt = cv.VideoCapture(0)

if not capt.isOpened():
    print("Erreur lors de l'ouverture")
    exit()

while True:
    ret, frame = capt.read() # frame.dims = (480, 640, 3)

    # Afficher l'image
    cv.imshow('Camera', frame)
    
    # Si le read est bon alors ret = true
    if not ret:
        print("Erreur lors de la lecture")
        break

    to_print = convert_frame(frame)

    # \033[H remet le curseur en haut à gauche
    print("\033[H" + to_print, end="")

    # quitter
    if cv.waitKey(1) == ord('q'):
        break

capt.release()
cv.destroyAllWindows()