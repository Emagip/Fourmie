from simul_sans_tk import *
import simul_tk_v2 as simu
import matplotlib.pyplot as plt
from tkinter import *


def graphique():
    '''créer un graphique nb_mouv par nb_simu.
    Sur le graphique apparait également la moyenne des mouvment de la fourmie et le temps qu'une simulation a prise
    '''
    plt.plot(nb_simu,
             nb_mouv,
             "bo--",
             label="nombre de mouvements")
    plt.plot(nb_simu, moy_len,
             "-",
             color="green",
             label="Moyenne au cour du temps")
    plt.plot([0, len(nb_simu)],
             [moyenne(), moyenne()],
             "r-",
             label=f"Moyenne finnale: {moyenne()}")
    plt.legend(loc='upper right')
    plt.ylabel("nombre de mouvement par simulation")
    plt.xlabel("nombre de simulation faite")
    plt.show()


def moyenne():
    '''calcul la moyenne du nombre de mouvment fait par rapport au nombre de simulations'''
    moy = round(mouv / int(simuls), 2)
    return moy


def simuTK():
    '''execute le programme main_tk qui est l'interface graphique du jeu'''
    global interface
    submit()
    detruire_btn_vitesse()
    simu.main_tk()


def submit():
    '''la fonction permet de prendre en compte les valeurs mises dans les cases dédier sur l'interface de jeu
    et de les donner au bonne variables, simuls prend le nombre de simulations à faire, delay prend le temps qu'il faut
     attendre entre chaque image '''
    global simuls, vitesse_var, delayval
    vitesses = [0.1,
                0.01,
                0.001,
                0.0001]
    simuls = simu_var.get()
    delaytemp = vitesse_var.get()
    delayval = int(delaytemp)
    simu.delay = vitesses[delayval]
    print('nb simulations = ',
          simuls,
          ', vitesse de la fourmi = ',
          simu.delay)


def combien_de_simu():
    '''fonction qui créer les boutons pour pouvoir donner le nombre de simulations voulu'''
    global simu_label, simu_entry, simu_var
    simu_var = StringVar()
    simu_label = Label(simu.Fond, 
                       text="combien de simulations voulez vous faire")
    simu_label.grid(row=4,column=0)
    simu_entry = Entry(simu.Fond, textvariable=simu_var)
    simu_entry.grid(row=5, column=0)


def vitesseFourmi():
    '''fonction qui créer les boutons pour pouvoir donner la vitesse voulu'''
    global vitesse_var, vitesse_label, vitesse_entry, vitesse_label2
    vitesse_var = StringVar(value='0')
    vitesse_label = Label(simu.Fond,
                          text="à quelle vitesse voulez vous que votre Fourmi ce déplace")
    vitesse_label.grid(row=0, column=0)
    vitesse_label2 = Label(simu.Fond,
                           text=" 0 : 0.1s (normal), 1 : 0.01s (rapide), 2 : 0.001 (trés rapide), 3 : 0.0001 (supersonique)")
    vitesse_label2.grid(row=1, column=0)
    vitesse_entry = Entry(simu.Fond, textvariable=vitesse_var)
    vitesse_entry.grid(row=2, column=0)


def detruire_btn_vitesse():
    '''Fonction permettant de détruire le bouton de réglage de la vitesse'''
    vitesse_entry.destroy()
    vitesse_label.destroy()
    vitesse_label2.destroy()


def detruire_btn_simu():
    simu_entry.destroy()
    simu_label.destroy()


def simulations():
    global nb_simu, nb_mouv, mouv, moy_len, simuls
    submit()
    nb_simu = [y for y in range(int(simuls))]
    mouv = 0
    nb_mouv = []
    moy_len = []

    for i in range(int(simuls)):
        cpt = main_sans_tk()
        mouv += cpt
        nb_mouv.append(cpt)
        moy_len.append(mouv / (i + 1))

    detruire_btn_simu()
    print("moyenne :", moyenne())
    graphique()


vitesseFourmi()
combien_de_simu()
JeuAffichage = Button(simu.Fond,
                      text='Lancer une simulation avec interface graphique',
                      command=simuTK)
JeuAffichage.grid(row=3, column=0)
JeuGraphique = Button(simu.Fond,
                      text='Lancer plusieurs simulations et obtenir des statistics',
                      command=simulations)
JeuGraphique.grid(row=6, column=0)


simu.Fond.pack()
simu.interface.mainloop()
