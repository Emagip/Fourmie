from simul_sans_tk import *
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np

interface = Tk()

interface.title("Bienvenue chez les ch'ti")
interface.config(bg='blue')


def graphique():
    plt.plot(nb_simu, nb_mouv, "bo--", label="nombre de mouvements")
    plt.plot(nb_simu, moy_len, "-", color="green", label="Moyenne au cour du temps")
    plt.plot([0, len(nb_simu)], [moyenne(), moyenne()], "r-", label=f"Moyenne finnale: {moyenne()}")
    plt.legend(loc='upper right')
    plt.ylabel("nombre de mouvement par simulation")
    plt.xlabel("nombre de simulation faite")
    plt.show()

def moyenne():
    moy = round(mouv/simu, 2)
    return moy

def simulations():
    global nb_simu, nb_mouv, mouv, simu, moy_len
    simu = int(input("donner le nombre de simulation à faire"))
    nb_simu = [y for y in range(simu)]
    mouv = 0 
    nb_mouv = []
    moy_len = []
    for i in range(simu):
        cpt = main()
        print(cpt)
        mouv+=cpt
        nb_mouv.append(cpt)
        moy_len.append(mouv/(i+1))
        
    print("moyenne :", moyenne())
    graphique()

def simuTK():
    import simul_tk

Cadre = Canvas(interface,bg="black",width=1000, height = 1000)

JeuAffichage = Button(Cadre,text='Lancer une simulation avec interface graphique', command = simuTK)
JeuAffichage.pack()
JeuGraphique = Button(Cadre,text='Lancer plusieurs simulations et obtenir des statistics', command = simulations)
JeuGraphique.pack()

Cadre.pack()

interface.mainloop()
