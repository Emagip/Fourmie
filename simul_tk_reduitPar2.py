from tkinter import *
from random import choice
from time import sleep

from Cases import *

interface = Tk()

interface.title("Bienvenue chez les ch'ti")
interface.config(bg='#d6eaf8')

Cadre = Canvas(interface,bg="#7fb3d5",width=500, height = 500)
Fond = Canvas(interface,bg="#d6eaf8",width=1000, height = 1000)

def echequier():
    """Fonction qui affiche l'échéquier sur lequel la fourmie se déplace à l'écran"""
    for i in range(0,500,200): #création de l'echequier
        for j in range(0,500,200):
            Rect = Cadre.create_rectangle(j,i,j+100,i+100, fill='#3498db')
            Rect = Cadre.create_rectangle(i+100,j+100,i+200,j+200, fill='#3498db')
def set_bonbon():
    """récupère l'image des bonbons et les affiche sur les cases du bas"""
    global Bonbon, Cadre_bonbon
    Cadre_bonbon = []
    Bonbon = PhotoImage(file="bonbon.png")
    for i in range(50,451, 100):  #ajout des bonbons
        Cadre_bonbon.append(Cadre.create_image(i, 450,image=Bonbon))

def set_fourmie():
    """ récupère l'image de la fourmie et l'affiche au centre de l'échequier"""
    global Cadre_fourmie, Fourmie
    Fourmie = PhotoImage(file="fourmie.png") 
    
    Cadre_fourmie = Cadre.create_image(250, 250, image=Fourmie)#ajout de la fourmie

def import_fourmie_bonbon():
    """ récupère l'image de la fourmie qui porte un bonbon sans l'afficher"""
    global Fourmie_bonbon
    Fourmie_bonbon = PhotoImage(file="fourmie_bonbon.png")

def set_fourmie_bonbon(x,y):
    """affiche la fourmie qui porte le bonbon aux coordonnées x,y fournies en paramètres"""
    Cadre.coords(Cadre_fourmie_bonbon, x, y)

def deplacement(fourmieAsBonbon):
    """déplace la fourmie aléatoirement selon les cases déterminées dans Cases.py"""
    direction = choice(plateau[coords[0]][coords[1]]['can_go'])
    coords[0] += direction[0]
    coords[1] += direction[1]
    x, y = GetCoords(coords)
    if not fourmieAsBonbon:
        Cadre.coords(Cadre_fourmie, x, y)
    else:
        set_fourmie_bonbon(x, y)
    Cadre.update()

def recupere_bonbon(x, y):
    """Si la fourmie passe sur un bonbon, celui-ci est supprimé ainsi que la fourmie qui est remplacée par l'image fourmie_bonbon"""
    global Cadre_fourmie_bonbon, fourmieAsBonbon
    plateau[coords[1]][coords[0]]['HasCandy'] = False
        
    Cadre.delete(Cadre_fourmie)
    Cadre.delete(Cadre_bonbon[coords[0]])
    Cadre.update()
    #ajout fourmie qui porte un bonbon
    Cadre_fourmie_bonbon = Cadre.create_image(x, y, image=Fourmie_bonbon)
    fourmieAsBonbon = True
    Cadre.update()

def pose_bonbon(x, y):
    """Crée une image de bonbon sur la case ou se trouve la fourmie si elle est sur une case du haut + remplace l'image fourmie_bonbon par fourmie"""
    global CaseHautBonbon, Cadre_fourmie, fourmieAsBonbon
    Cadre.create_image(x, y,image=Bonbon)
    CaseHautBonbon[coords[0]] = True
    Cadre.delete(Cadre_fourmie_bonbon)
    Cadre_fourmie = Cadre.create_image(x, y, image=Fourmie)
    Cadre.update()
    fourmieAsBonbon = False

def ini():
    """Initialisation de la simulation"""
    global CaseHautBonbon,fourmieAsBonbon,coords
    echequier()
    set_bonbon()
    set_fourmie()
    import_fourmie_bonbon()
    
    CaseHautBonbon = [False, False, False, False, False]
    fourmieAsBonbon = False
    coords = [2,2]

def main_tk():
    """simulation principale"""
    global compteur, plateau
    plateau = set()

    ini()
    
    x, y = GetCoords(coords)

    Cadre.pack()
    while CaseHautBonbon != [True, True, True, True, True]:
        deplacement(fourmieAsBonbon)
        x, y = GetCoords(coords)
        #si elle arrive sur une case avec un bonbon
        if plateau[coords[1]][coords[0]]['HasCandy'] and not fourmieAsBonbon:
            recupere_bonbon(x, y)

        #si elle arrive sur une case du haut et qu'elle a un bonbon
        if coords[1] == 0 and fourmieAsBonbon and not CaseHautBonbon[coords[0]]:
            pose_bonbon(x, y)

        sleep(delay)

        compteur += 1

compteur = 0
delay = 0.1


