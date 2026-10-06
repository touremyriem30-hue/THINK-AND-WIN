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


# PHASE 2 : EXECUTION ET NAVIGATION DU QUIZ

bonnes_reponses = 0
mauvaises_reponses = 0

def question_suivante():
    global numero

    numero += 1

    if numero < nombre_questions:
        Afficher_question(numero)
    else:
        print("Quiz terminé")
        print("Votre score est :", score)
        print("Bonnes réponses :", bonnes_reponses)
        print("Mauvaises réponses :", mauvaises_reponses)


def verifier_reponse(resultat):
    global bonnes_reponses, mauvaises_reponses

    if resultat == contenu[numero]["REPONSE"]:
        print("Youpiii vous avez réussi")
        bonnes_reponses += 1
        Gestion_score(True)

    else:
        print("Oups vous avez échoué")
        mauvaises_reponses += 1
        Gestion_score(False)

    question_suivante()

# Mettre à jour le score
def Gestion_score(resultat_verification):
    global score

    if resultat_verification:
        score += 1

# Relier les boutons à la vérification
bouton1.config(command=lambda: verifier_reponse(bouton1["text"]))
bouton2.config(command=lambda: verifier_reponse(bouton2["text"]))
bouton3.config(command=lambda: verifier_reponse(bouton3["text"]))
bouton4.config(command=lambda: verifier_reponse(bouton4["text"]))

window.mainloop()