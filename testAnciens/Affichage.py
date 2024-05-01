from tkinter import *
from Statistics_v1 import simulations
from main_v3 import *


acceuil = Tk()
acceuil.title('bienvenue sur le jeux de la fourmie !')
acceuil.config(bg='blue',height=250,width=250)
Cadre = Canvas(acceuil,bg="white",width=1000, height = 1000)


JeuAffichage = Button(Cadre,text='Lancer une simulation avec interface graphique', command = main())
JeuAffichage.pack()
JeuGraphique = Button(Cadre,text='Lancer plusieurs simulations et obtenir des statistics', command = simulations())
JeuGraphique.pack()


acceuil.mainloop()
