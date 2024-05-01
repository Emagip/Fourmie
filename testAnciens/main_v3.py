from tkinter import *
from random import choice
from time import sleep

from Cases import *


Simu = Tk()


Simu.title("Pas bête la bête")
Simu.config(bg="orange")

Cadre = Canvas(Simu,bg="white",width=1000, height = 1000)

def echequier():
    for i in range(0,1000,400): #création de l'echequier
        for j in range(0,1000,400):
            Rect = Cadre.create_rectangle(j,i,j+200,i+200, fill='blue')
            Rect = Cadre.create_rectangle(i+200,j+200,i+400,j+400, fill='blue')
def set_bonbon():
    global Bonbon, Cadre_bonbon
    Cadre_bonbon = []
    Bonbon = PhotoImage(file="bonbon.png")
    for i in range(100,901, 200):  #ajout des bonbons
        Cadre_bonbon.append(Cadre.create_image(i, 900,image=Bonbon))

def set_fourmie():
    global Cadre_fourmie, Fourmie
    Fourmie = PhotoImage(file="fourmie.png") 
    
    Cadre_fourmie = Cadre.create_image(500, 500, image=Fourmie)#ajout de la fourmie

def import_fourmie_bonbon():
    global Fourmie_bonbon
    Fourmie_bonbon = PhotoImage(file="fourmie_bonbon.png")

def set_fourmie_bonbon(x,y):
    Cadre.coords(Cadre_fourmie_bonbon, x, y)

def deplacement(fourmieAsBonbon):
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
    global CaseHautBonbon, Cadre_fourmie,fourmieAsBonbon
    Cadre.create_image(x, y,image=Bonbon)
    CaseHautBonbon[coords[0]] = True
    Cadre.delete(Cadre_fourmie_bonbon)
    Cadre_fourmie = Cadre.create_image(x, y, image=Fourmie)
    Cadre.update()
    fourmieAsBonbon = False

def main():
    global compteur
    echequier()
    set_bonbon()
    set_fourmie()
    import_fourmie_bonbon()
    
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

        sleep(0.0001)
        compteur += 1

CaseHautBonbon = [False, False, False, False, False]
fourmieAsBonbon = False
coords = [2,2]
compteur = 0


Simu.mainloop()


