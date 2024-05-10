from simul_sans_tk import *
import simul_tk_reduitPar2 as simu
import matplotlib.pyplot as plt
from tkinter import *


def graphique():
    '''créer un graphique du nombre de mouvement par le nombre de simulation.
    Sur le graphique apparait également la moyenne des mouvment de la fourmie
    et la duree d'une simulation
    '''
    plt.plot(nb_simu, nb_mouv,
             "bo--",
             label="nombre de mouvements"
             )
    plt.plot(nb_simu, moy_len,
             "-", color="green",
             label="Moyenne au cour du temps"
             )
    plt.plot([0, len(nb_simu)],
             [moyenne(), moyenne()],
             "r-",
             label=f"Moyenne finnale: {moyenne()}"
             )
    plt.legend(loc='upper right')
    plt.ylabel("nombre de mouvement par simulation")
    plt.xlabel("nombre de simulation faite")
    plt.show()


def moyenne():
    '''calcul la moyenne du nombre de mouvment par le nombre de simulations'''
    moy = round(mouv / simuls, 2)
    return moy


def submit_vitesse():
    '''la fonction permet de prendre en compte les valeurs mises dans les cases dédier sur l'interface de jeu
    et de les donner au bonne variables delay prend le temps qu'il faut attendre entre chaque mouvement de la fourmie '''
    vitesse_var
    vitesses = [0.1,0.01,0.001,0.0001]
    delayval = vitesse_var.get()
    simu.delay = vitesses[delayval]
    print('vitesse de la fourmi = ',simu.delay)


def submit_simul():
    '''la fonction permet de prendre en compte les valeurs mises dans les cases dédier sur l'interface de jeu
    et de les donner au bonne variables, simuls prend le nombre de simulations à faire'''
    global simuls
    simuls = simu_var.get()
    print('nb simulations = ',simuls,)


def combien_de_simu():
    '''fonction qui créer les boutons pour pouvoir donner le nombre de simulations voulu'''
    global simu_label,simu_entry,simu_var
    simu_var = IntVar()
    simu_label = Label(simu.Fond,text="combien de simulations voulez vous faire")
    simu_label.grid(row=4,column=0)
    simu_entry = Entry(simu.Fond, textvariable= simu_var)
    simu_entry.grid(row=5,column=0)


def vitesseFourmi():
    '''fonction qui créer les boutons pour pouvoir donner la vitesse voulu'''
    global vitesse_var,vitesse_label,vitesse_entry,vitesse_label2
    vitesse_var = IntVar()
    vitesse_label = Label(simu.Fond,text="À qu'elle vitesse voulez vous que votre fourmi ce déplace")
    vitesse_label.grid(row=0,column=0)
    vitesse_label2 = Label(simu.Fond,text=" 0 : 0.1s (normal), 1 : 0.01s (rapide), 2 : 0.001 (trés rapide), 3 : 0.0001 (supersonique)")
    vitesse_label2.grid(row=1,column=0)
    vitesse_entry = Entry(simu.Fond, textvariable= vitesse_var)
    vitesse_entry.grid(row=2,column=0)


def detruire_btn_vitesse():
    '''fonction qui détruit les boutons temporaire pour la vitesse'''
    vitesse_entry.destroy()
    vitesse_label.destroy()
    vitesse_label2.destroy()
    JeuAffichage.config(text='Lancer une simulation avec interface graphique', command = MiseEnPlaceTK)


def detruire_btn_simu():
    '''fonction qui détruit les boutons temporaire pour le nombre simulations'''
    simu_entry.destroy()
    simu_label.destroy()
    JeuGraphique.config(text='Lancer plusieurs simulations et obtenir des statistics',command=simuSansTK)


def stats():
    '''fonction qui utilise la fonction moyenne, graphique et de main_sans_tk pour faire un graphique avec le nombre de simulations et le nombre de
    mouvment fait par la fourmi'''
    global nb_simu, nb_mouv, mouv, moy_len,simuls
    
    submit_simul()

    nb_simu = [y for y in range(simuls)]
    mouv = 0 
    nb_mouv = []
    moy_len = []

    for i in range(simuls):
        cpt = main_sans_tk()
        mouv+=cpt
        nb_mouv.append(cpt)
        moy_len.append(mouv/(i+1))
    
    detruire_btn_simu()
    print("moyenne :", moyenne())
    graphique()


def simuSansTK():
    '''lance les fonctions permettant de faire des simulations sans interface et avoir toutes les statistics derrière'''
    global simuls
    combien_de_simu()
    JeuGraphique.config(text='valider',command=stats)


def MiseEnPlaceTK():
    '''execute le programme main_tk qui est l'interface graphique du jeu'''
    vitesseFourmi()
    JeuAffichage.config(text='valider', command=simuTK)


def simuTK():
    '''execute le programme main_tk qui est l'interface graphique du jeu'''
    global interface
    submit_vitesse()
    simu.main_tk()
    detruire_btn_vitesse()


#création des boutton principaux1
JeuAffichage = Button(simu.Fond,text='Lancer une simulation avec interface graphique', command = MiseEnPlaceTK)
JeuAffichage.grid(row=3,column=0)
JeuGraphique = Button(simu.Fond,text='Lancer plusieurs simulations et obtenir des statistics', command = simuSansTK)
JeuGraphique.grid(row=6,column=0)
Quitter = Button(simu.Fond,text='Quitter le jeu', command=simu.interface.destroy)
Quitter.grid(row=7,column=0)


simu.Fond.pack()
simu.interface.mainloop()
