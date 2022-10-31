#!/usr/bin/env python3
# pylint: disable-R0915
"Génére des images PPM montrant la simulation de Monte carlos \
pour approximer pi ! et les compile en GIF "
import sys
import subprocess
from math import floor
from numpy import array
import simulator



def genere_ppm_file(taille, simulation, nb_virg, matrice_de_pixel, numero_image):
    "Generer des images ppm"
    chiffre, lin, lout = simulation[0], simulation[1], simulation[2]
    chiffre = str(chiffre)[:nb_virg + 2]
    while len(chiffre) < (nb_virg + 2):
        #Pour completer par des 0 jusqu'a la précision demandé.
        chiffre = chiffre + '0'
    for i in lin:
        #Pour dimmensionner les points et les adapter à la taille de l'image
        cor_x = floor(i[0]*taille//2) + taille // 2
        cor_y = taille // 2  - floor(i[1]* (taille // 2)) - 1
        #Pour positionner les points intérieurs dans la matrice.
        matrice_de_pixel[cor_y][cor_x] = 1
    for i in lout:
        #Pour positionner les points extérieurs dans la matrice
        cor_x = floor(i[0] * taille // 2) + taille // 2
        cor_y = taille // 2 - floor(i[1] * (taille // 2)) - 1
        matrice_de_pixel[cor_y][cor_x] = -1
    matrice_de_pixel_2 = matrice_de_pixel.copy() #copie de matrice qui contient que les points
    for i in enumerate(chiffre):
        ecrire(i[1], matrice_de_pixel, i[0], taille, nb_virg)
    with open("img"+str(numero_image)+"_" + chiffre[0] + '-' + chiffre[2:nb_virg + 2]
              + '.ppm', 'wb') as file:
        file.write(bytes(f"P6 {taille} {taille} 255 ", 'ascii'))
        for ligne in matrice_de_pixel:
            for element in ligne:
                #"Parcourir la matrice pour colorier chaque pixel"
                if element == 1:
                    file.write(bytearray([250, 85, 85]))
                elif element == -1:
                    file.write(bytearray([86, 21, 180]))
                elif element == 0:
                    file.write(bytearray([255, 255, 255]))
                else:
                    file.write(bytearray([0, 0, 0]))
    return matrice_de_pixel_2
def ecrire(chiffre, matrice, ordre, taille, nbr_vir):
    "changer la matrice de pixel de façon qu'elle montre le chiffre dans l'image"\
    # "Sa commence par calculer la taille des caractéres et leurs places"
    demi_taille, alpha = len(matrice) // 2, (taille //90 + 1)
    # Alpha est l'epaisseur de chaque caractére
    min_cor_x = demi_taille -(5 * alpha + - 1) // 2
    min_cor_y = (4 * alpha) * ordre - (nbr_vir - 1 - taille // 100)\
    * 2 * alpha + demi_taille // 2 + (90//taille)*alpha
    if int(taille) < 501:
        min_cor_y = min_cor_y + taille // 8
    if int(taille) > 900:
        min_cor_y = min_cor_y - taille // 8
    caractere(chiffre, matrice, alpha, min_cor_x, min_cor_y)


def caractere(chiffre, matrice, alpha, min_cor_x, min_cor_y):
    "Insére dans la matrice le caractére rensigné ."
    if chiffre == '.':
        matrice[min_cor_x+4*alpha:min_cor_x+5*alpha, min_cor_y+alpha: min_cor_y + 2 * alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
    elif chiffre == '3':
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y+ 2 * alpha:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])
        matrice[min_cor_x:min_cor_x + alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 2 * alpha:min_cor_x + 3 * alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 4 * alpha:min_cor_x + 5 * alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
    elif chiffre == '1':
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y + 2 * alpha:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])

    elif chiffre == '4':
        matrice[min_cor_x:min_cor_x + 3 * alpha, min_cor_y:min_cor_y + alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 3*alpha)])
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y + 2 * alpha:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])
        matrice[min_cor_x + 2 * alpha:min_cor_x + 3 * alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])

    elif chiffre == '5':
        matrice[min_cor_x:min_cor_x + alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 4 * alpha:min_cor_x + 5 * alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 2 * alpha:min_cor_x + 3 * alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3 * alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + alpha:min_cor_x + 2 * alpha, min_cor_y:min_cor_y + alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x+3*alpha:min_cor_x+4*alpha, min_cor_y+2*alpha:min_cor_y+3*alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])

    elif chiffre == '2':
        matrice[min_cor_x:min_cor_x + alpha, min_cor_y:min_cor_y + 3 * alpha] \
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 4 * alpha:min_cor_x + 5 * alpha, min_cor_y:min_cor_y + 3 * alpha] \
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 2 * alpha:min_cor_x + 3 * alpha, min_cor_y:min_cor_y + 3 * alpha] \
            = array([[2 for _ in range(0, 3 * alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + alpha:min_cor_x + 2 * alpha, min_cor_y + 2 * alpha:min_cor_y+3*alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 3 * alpha:min_cor_x+4*alpha, min_cor_y:min_cor_y + alpha] = array(
            [[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
    elif chiffre == '6':
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y:min_cor_y + alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])
        matrice[min_cor_x+2*alpha:min_cor_x+5*alpha, min_cor_y + 2 * alpha:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 3*alpha)])
        matrice[min_cor_x + 2 * alpha:min_cor_x + 3 * alpha, min_cor_y + alpha:min_cor_y +2*alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 4 * alpha:min_cor_x + 5 * alpha, min_cor_y + alpha:min_cor_y +2*alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x:min_cor_x + alpha, min_cor_y:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])

    elif chiffre == '7':
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y+ 2 * alpha:min_cor_y +3*alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])
        matrice[min_cor_x:min_cor_x + alpha, min_cor_y:min_cor_y+3*alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 2 * alpha:min_cor_x + 3 * alpha, min_cor_y:min_cor_y +3*alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
    elif chiffre == '8':
        caractere('6', matrice, alpha, min_cor_x, min_cor_y)
        matrice[min_cor_x + 3*alpha:min_cor_x + 5*alpha, min_cor_y:min_cor_y + alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 2*alpha)])
    elif chiffre == '9':
        matrice[min_cor_x:min_cor_x + 3 * alpha, min_cor_y: min_cor_y + alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 3*alpha)])
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y + 2 * alpha:min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])
        matrice[min_cor_x:min_cor_x + alpha, min_cor_y + alpha:min_cor_y + 2 * alpha]\
            = array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 2 * alpha:min_cor_x + 3 * alpha, min_cor_y: min_cor_y + 3 * alpha]\
            = array([[2 for _ in range(0, 3*alpha)] for _ in range(0, alpha)])
    else: #0
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y: min_cor_y + alpha] = array(
            [[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])
        matrice[min_cor_x:min_cor_x + 5 * alpha, min_cor_y + 2 * alpha:min_cor_y + 3 * alpha] = \
            array([[2 for _ in range(0, alpha)] for _ in range(0, 5*alpha)])
        matrice[min_cor_x:min_cor_x + alpha, min_cor_y + alpha:min_cor_y + 2 * alpha] = array(
            [[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
        matrice[min_cor_x + 4 * alpha:min_cor_x + 5 * alpha, min_cor_y\
                    + alpha:min_cor_y + 2 * alpha] = \
                    array([[2 for _ in range(0, alpha)] for _ in range(0, alpha)])
def ppm2gif(image_str, output_gif):
    "convertir des images jpg ou png ou ppm en GIF"
    str1 = f"convert -delay 100 -loop 1 {image_str} {output_gif}"
    subprocess.call(str1, shell=True)



def main():
    """Execute le script si lancé seul"""
    if len(sys.argv) != 4:
        raise IndexError(
        "Le programme doit recevoir en argument 3 donnés:Taille de l'image,nombre de point"
        ", nombre de chiffre à afficher.")
    for indice in range(1,4):
        for caractére in sys.argv[indice]:
            if ord(caractére)<48 or ord(caractére)>57:
                raise ValueError(
                "Un caractére est non reconnu"
                "(Peut être vous avez entré un nombre négative, ou non naturel,"
                " ou un caractére qui ne correspond pas à un chiffre)"
                " merci d'entrer 3 entiers naturels")
    if not 0 < int(sys.argv[3]) <= 12:
        raise ValueError("Le nombre de chiffres à afficher aprés la virgule "
                         "doit être compris entre 1 et 12.")
    if int(sys.argv[1]) <= 50:
        raise ValueError("Taille minimal : 50x50.")
    if int(sys.argv[2]) <= 1000:
        raise ValueError("Nombre de point minimal est 1000.")
    taille, nb_pt, nb_vir = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    compteur = 0
    numero_image, matrice = 0, array([[0 for _ in range(0, taille)] for _ in range(0, taille)])
    for k in range(1, 11):
        numero_image += 1
        simulation = simulator.simulation(k*nb_pt//10, compteur, nb_pt//10)
        compteur = simulation[1]
        pti = simulation[2]
        pto = simulation[3]
        approximation = simulation[0]
        matrice = genere_ppm_file(taille, (approximation, pti, pto), nb_vir, matrice, k)
     #   print('Image numéro '+ str(numero_image) + '/10 générée.')
    ppm2gif("img*_*-**.ppm", "animatedGif.gif")
    #print('Image GIF  générée.')
if __name__ == "__main__":
    # execute only if run as a script
    main()
