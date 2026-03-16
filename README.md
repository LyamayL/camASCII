# camASCII
Projet Personnel – 15/16 Mars 2026

🇫🇷 - Présentation
CamAscii est un outil de visualisation en temps réel qui transforme le flux de votre webcam en art ASCII dynamique directement dans la console.

En utilisant des algorithmes de traitement d'image et les capacités de rendu "True Color" des terminaux modernes, ce projet explore la conversion de données matricielles complexes en une représentation textuelle stylisée.

Ce projet permet d'observer comment la résolution, le contraste et la gestion des couleurs influencent la perception d'une image à travers une grille de caractères limités.
Principe de fonctionnement

    Capture et Prétraitement :
    Le flux est capturé en direct via la webcam. Chaque image est redimensionnée pour s'adapter à la largeur du terminal. Pour éviter l'étirement vertical (les caractères étant plus hauts que larges), un facteur de correction de 0.5 est appliqué à la hauteur.

    Mapping de Luminosité :
    Chaque pixel est converti en valeur de gris (0 à 255). Cette valeur est ensuite mappée sur une palette de densité de caractères :
    @ % # * + = - : . 
    Les zones sombres reçoivent des caractères denses (@), tandis que les zones claires reçoivent des caractères discrets (.).

    Rendu True Color (ANSI) :
    Contrairement aux anciens rendus ASCII en noir et blanc, CamAscii utilise les séquences d'échappement ANSI \033[38;2;R;G;Bm.

        Le script extrait les composantes Rouge, Vert, Bleu de chaque pixel original.

        Il injecte ces valeurs directement avant chaque caractère ASCII.

        Le résultat est une image texturée qui conserve la fidélité colorimétrique de la source.

    Optimisation de l'affichage :
    Pour garantir un flux fluide, le script utilise la commande \033[H pour repositionner le curseur en haut à gauche sans effacer l'écran, évitant ainsi tout clignotement visuel.

Technologies

    Python

    OpenCV – traitement de flux vidéo et manipulation de matrices d'images

    NumPy – calculs vectorisés pour le traitement rapide des données

    ANSI Escape Codes – rendu graphique avancé dans l'interface de commande (CLI)

🇬🇧 - Overview
CamAscii is a real-time visualization tool that transforms your webcam feed into dynamic ASCII art directly within the console.

By using image processing algorithms and the "True Color" rendering capabilities of modern terminals, this project explores the conversion of complex matrix data into a stylized textual representation.

This project allows observing how resolution, contrast, and color management influence image perception through a grid of limited characters.
How it works

    Capture and Preprocessing:
    The feed is captured live via the webcam. Each frame is resized based on the terminal width. To prevent vertical stretching (as characters are taller than they are wide), a correction factor of 0.5 is applied to the height.

    Luminosity Mapping:
    Each pixel is converted to a grayscale value (0 to 255). This value is then mapped to a character density palette:
    @ % # * + = - : . 
    Dark areas receive dense characters (@), while bright areas receive subtle ones (.).

    True Color Rendering (ANSI):
    Unlike old black-and-white ASCII renders, CamAscii uses ANSI escape sequences \033[38;2;R;G;Bm.

        The script extracts the Red, Green, Blue components of each original pixel.

        It injects these values directly before each ASCII character.

        The result is a textured image that maintains the color fidelity of the source.

    Display Optimization:
    To ensure a smooth stream, the script uses the \033[H command to reposition the cursor at the top-left without clearing the screen, preventing any visual flickering.

Technologies

    Python

    OpenCV – video stream processing and image matrix manipulation

    NumPy – vectorized calculations for fast data processing

    ANSI Escape Codes – advanced graphical rendering in the Command Line Interface (CLI)
