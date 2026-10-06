# PHASE 1 : INITIALISATION ET CHARGEMENT DES DONNEES DU QUESTIONNAIRE

import json as js
import tkinter as tk

# Chargement des données du quiz
fichier = open("INFO.json", "r", encoding = "utf-8")
contenu = js.load(fichier)
fichier.close()

# Variables du quiz
score = 0
numero = 0
nombre_questions = 3

# Création de la fenêtre
window = tk.Tk()
window.title("THINK AND WIN")
window.geometry("500x400")

# Affichage de la question
label_question = tk.Label(window, text="")
label_question.pack()

# Options de réponse
bouton1 = tk.Button(window, text="")
bouton1.pack()

bouton2 = tk.Button(window, text="")
bouton2.pack()

bouton3 = tk.Button(window, text="")
bouton3.pack()

bouton4 = tk.Button(window, text="")
bouton4.pack()

# Afficher une question et ses options
def Afficher_question(numero):
    question = contenu[numero]

    label_question.config(text=question["QUESTION"])

    bouton1.config(text=question["OPTION"][0])
    bouton2.config(text=question["OPTION"][1])
    bouton3.config(text=question["OPTION"][2])
    bouton4.config(text=question["OPTION"][3])

# Afficher la première question
Afficher_question(0)

window.mainloop()
