from random import choice
import Cases as cases


def deplacement(coords):
    direction = choice(plateau[coords[0]][coords[1]]['can_go'])
    coords[0] += direction[0]
    coords[1] += direction[1]
    return coords


def recupere_bonbon(fourmieAsBonbon, coords):
    plateau[coords[1]][coords[0]]['HasCandy'] = False
    # ajout fourmie qui porte un bonbon
    fourmieAsBonbon = True
    return fourmieAsBonbon


def pose_bonbon(CaseHautBonbon, coords, fourmieAsBonbon):
    CaseHautBonbon[coords[0]] = True
    fourmieAsBonbon = False
    return fourmieAsBonbon


def main():
    global plateau
    plateau = cases.set()
    compteur = 0
    coords = [2, 2]
    fourmieAsBonbon = False
    CaseHautBonbon = [False, False, False, False, False]
    while CaseHautBonbon != [True, True, True, True, True]:
        coords = deplacement(coords)
        # si elle arrive sur une case avec un bonbon
        if plateau[coords[1]][coords[0]]['HasCandy'] and not fourmieAsBonbon:
            fourmieAsBonbon = recupere_bonbon(fourmieAsBonbon, coords)

        # si elle arrive sur une case du haut et qu'elle a un bonbon
        if coords[1] == 0 and fourmieAsBonbon and not CaseHautBonbon[coords[0]]:
            fourmieAsBonbon = pose_bonbon(
                CaseHautBonbon,
                coords,
                fourmieAsBonbon
            )
        compteur += 1
    return compteur
