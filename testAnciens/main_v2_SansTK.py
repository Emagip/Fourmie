from random import choice
from time import sleep

from Cases import *

def set_bonbon():
    global Bonbon, Cadre_bonbon
    Cadre_bonbon = []

def deplacement(fourmieAsBonbon):
    direction = choice(plateau[coords[0]][coords[1]]['can_go'])
    coords[0] += direction[0]
    coords[1] += direction[1]
    x, y = GetCoords(coords)

def recupere_bonbon(x, y):
    global Cadre_fourmie_bonbon, fourmieAsBonbon
    plateau[coords[1]][coords[0]]['HasCandy'] = False
    fourmieAsBonbon = True    

def pose_bonbon(x, y):
    CaseHautBonbon[coords[0]] = True
    fourmieAsBonbon = False
   

def main():
    global fourmieAsBonbon,coords,CaseHautBonbon
    compteur = 0
    set_bonbon()
    
    x, y = GetCoords(coords)

    while CaseHautBonbon != [True, True, True, True, True]:
        deplacement(fourmieAsBonbon)
        x, y = GetCoords(coords)
        #si elle arrive sur une case avec un bonbon
        if plateau[coords[1]][coords[0]]['HasCandy'] and not fourmieAsBonbon:
            recupere_bonbon(x, y)

        #si elle arrive sur une case du haut et qu'elle a un bonbon
        if coords[1] == 0 and fourmieAsBonbon and not CaseHautBonbon[coords[0]]:
            pose_bonbon(x, y)
        compteur += 1

    #remise à zero
    CaseHautBonbon = [False, False, False, False, False]
    fourmieAsBonbon = False
    coords = [2,2]
    return compteur


CaseHautBonbon = [False, False, False, False, False]
fourmieAsBonbon = False
coords = [2,2]
