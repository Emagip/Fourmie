from simul_sans_tk import *
import simul_tk_v2 as simu


import matplotlib.pyplot as plt
from tkinter import *
import numpy as np



def graphique():
    plt.plot(nb_simu, nb_mouv, "bo--", label="nombre de mouvements")
    plt.plot(nb_simu, moy_len, "-", color="green", label="Moyenne au cour du temps")
    plt.plot([0, len(nb_simu)], [moyenne(), moyenne()], "r-", label=f"Moyenne finnale: {moyenne()}")
    plt.legend(loc='upper right')
    plt.ylabel("nombre de mouvement par simulation")
    plt.xlabel("nombre de simulation faite")
    plt.show()

def moyenne():
    moy = round(mouv/int(simu), 2)
    return moy

def simulations():
    global nb_simu, nb_mouv, mouv, simu, moy_len,simu_var
    '''
    simu_var = StringVar()
    simu_label = Label(simu.Cadre, text='donner le nombre de simulation à faire ') 
    simu_label.pack()
    simu_entry = Entry(Fond, textvariable= simu_var)
    simu_entry.pack()
    sub_btn=Button(Fond,text = 'Submit', command = submit)
    sub_btn.pack()
    '''
    
    simu = int(input('nombre de simulations à effectuer : '))

    nb_simu = [y for y in range(int(simu))]
    mouv = 0 
    nb_mouv = []
    moy_len = []

    for i in range(int(simu)):
        cpt = main_sans_tk()
        print(cpt)
        mouv+=cpt
        nb_mouv.append(cpt)
        moy_len.append(mouv/(i+1))
        
    print("moyenne :", moyenne())
    graphique()


def simuTK():
    global interface
    simu.main_tk()

def submit():
    nb_deboucle = simu_var.get()
    return nb_deboucle

JeuAffichage = Button(simu.Fond,text='Lancer une simulation avec interface graphique', command = simuTK)
JeuAffichage.pack()
JeuGraphique = Button(simu.Fond,text='Lancer plusieurs simulations et obtenir des statistics', command = simulations)
JeuGraphique.pack()
simu.Fond.pack()
simu.interface.mainloop()
