#! /usr/bin/env python3
"fait une simulation de Pi ! "
from random import uniform
import sys




def norme(liste):
    "la distance du point au centre"
    return (liste[0])**2 + (liste[1]**2)
def simulation(nombre_de_points_total, compteur, nombre_de_point):
    "génére les points aléatoires et récupére l'approximation atteinte"
    lin, lout = [], []
    for _ in range(0, nombre_de_point):
        nombre_aleatoire = [uniform(-1, 1), uniform(-1, 1)]
        if norme(nombre_aleatoire) <= 1:
            compteur += 1
            lin.append(nombre_aleatoire)
        if norme(nombre_aleatoire) > 1:
            lout.append(nombre_aleatoire)
    approximation = compteur*4/(nombre_de_points_total)
    return [approximation, compteur, lin, lout]

def main():
    "Retourne la valeur du compteur et les listes des points In et points Out "
    if len(sys.argv) != 2:
        raise IndexError(
            "Le programme doit recevoir en argument une seule donné"
            ":nombre de points.")
    for caractére in sys.argv[1]:
        if ord(caractére)<48 or ord(caractére)>57:
            raise ValueError(
            "Un caractére est non reconnu"
            "(Peut être vous avez entré un nombre négative, ou non naturel"
            " ou un caractére qui ne correspond pas à un chiffre).")
    if int(sys.argv[1]) <= 1000:
        raise ValueError("Nombre de point minimal est 1000.")
    nombre_de_simulation = int(sys.argv[1])
    print(simulation(nombre_de_simulation, 0, nombre_de_simulation)[0])
if __name__ == "__main__":
    # execute only if run as a script
    main()
