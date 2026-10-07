import json as js
import tkinter as tk

fichier = open("INFO.json", "r", encoding = "utf-8")
contenu = js.load(fichier)
fichier.close()

def recuperer_questions(niveau):
    questions = []

    for question in contenu:
        if question["NIVEAU"] == niveau:
            questions.append(question)

    return questions

numero = 0
score = 0
nombre_questions = 3
niveau = ""
bonnes_reponses = 0
mauvaises_reponses = 0

def question_suivante():
    global numero

    numero += 1

    if numero < nombre_questions :
        Afficher_question(numero)
    else:
       
        label_question.pack_forget()
        bouton1.pack_forget()
        bouton2.pack_forget()
        bouton3.pack_forget()
        bouton4.pack_forget()

        label_progression.config(text="QUIZ TERMINÉ")
        
        label_feedback.config(
            text=f"Score : {score}/{nombre_questions}\n"
                 f"Bonnes réponses : {bonnes_reponses}\n"
                 f"Mauvaises réponses : {mauvaises_reponses}"
        )
        label_feedback.pack(pady=20)

window = tk.Tk()
window.title("THINK AND WIN")
window.geometry("600x500")
window.config(bg="#FFF4FD")

label_bienvenue = tk.Label(
    window,
    text="Bienvenue dans THINK AND WIN !",
    font=("Arial", 24, "bold"),
    bg="#FFF4F7"
)
label_bienvenue.pack(pady=80)

label_description = tk.Label(
    window,
    text="Teste tes connaissances et amuse-toi !",
    font=("Arial", 13),
    bg="#FFF4F7"
)
label_description.pack(pady=10)

label_niveau = tk.Label(
    window,
    text="Choisissez votre niveau",
    font=("Arial", 16, "bold"),
    bg="#FFF4F7"
)
label_niveau.pack(pady=15)

def commencer():
    label_bienvenue.pack_forget()
    label_description.pack_forget()
    btn_commencer.pack_forget()

    label_prenom = tk.Label(
        window,
        text="Quel est votre prénom ?",
        font=("Arial", 18, "bold"),
        bg="#FFF4F7"
    )
    label_prenom.pack(pady=60)

    ent_prenom = tk.Entry(
        window,
        font=("Arial", 13),
        width=25
    )
    ent_prenom.pack(pady=10)

    def passer_au_niveau():
        prenom = ent_prenom.get()

        if not prenom.isalpha():
             label_prenom.config(
                 text="Veuillez entrer un prénom sans chiffres !",
                 fg="red"
             )
             return

        label_prenom.pack_forget()
        ent_prenom.pack_forget()
        btn_suivant.pack_forget()

        label_niveau.pack(pady=60)

        btn_facile.pack(pady=5)
        btn_difficile.pack(pady=5)
        btn_tres_difficile.pack(pady=5)

    btn_suivant = tk.Button(
        window,
        text="SUIVANT",
        font=("Arial", 12, "bold"),
        width=15,
        command=passer_au_niveau
    )
    btn_suivant.pack(pady=25)

btn_commencer = tk.Button(
    window,
    text="COMMENCER",
    font=("Arial", 12, "bold"),
    width=20,
    command = commencer
)
btn_commencer.pack(pady=30)

def choisir_facile():
    global niveau, questions
    niveau = "Facile"
    questions = recuperer_questions(niveau)
    print("Niveau choisi :", niveau)

    label_niveau.pack_forget()

    label_progression.pack(pady=10)

    label_score.pack(pady=5)

    label_feedback.pack(pady=5)
    
    label_question.pack(pady=25)

    bouton1.pack(pady=5)
    bouton2.pack(pady=5)
    bouton3.pack(pady=5)
    bouton4.pack(pady=5)
    
    label_niveau.pack_forget()

    btn_facile.pack_forget()
    btn_difficile.pack_forget()
    btn_tres_difficile.pack_forget()

    Afficher_question(0)

def choisir_difficile():
    global niveau, questions
    niveau = "Difficile"
    questions = recuperer_questions(niveau)
    print("Niveau choisi :", niveau)

    label_niveau.pack_forget()

    label_progression.pack(pady=10)

    label_score.pack(pady=5)

    label_feedback.pack(pady=5)

    label_question.pack(pady=25)

    bouton1.pack(pady=5)
    bouton2.pack(pady=5)
    bouton3.pack(pady=5)
    bouton4.pack(pady=5)

    label_niveau.pack_forget()

    btn_facile.pack_forget()
    btn_difficile.pack_forget()
    btn_tres_difficile.pack_forget()

    Afficher_question(0)

def choisir_tres_difficile():
    global niveau, questions
    niveau = "Très difficile"
    questions = recuperer_questions(niveau)
    print("Niveau choisi :", niveau)

    label_niveau.pack_forget()

    label_progression.pack(pady=10)

    label_score.pack(pady=5)

    label_feedback.pack(pady=5)

    label_question.pack(pady=25)

    bouton1.pack(pady=5)
    bouton2.pack(pady=5)
    bouton3.pack(pady=5)
    bouton4.pack(pady=5)

    label_niveau.pack_forget()

    btn_facile.pack_forget()
    btn_difficile.pack_forget()
    btn_tres_difficile.pack_forget()

    Afficher_question(0)

btn_facile = tk.Button(window, text="Facile", command = choisir_facile)
btn_facile.pack()

btn_difficile = tk.Button(window, text="Difficile", command = choisir_difficile)
btn_difficile.pack()

btn_tres_difficile = tk.Button(window, text="Très difficile", command = choisir_tres_difficile)
btn_tres_difficile.pack()

label_question = tk.Label(
    window,
    text="",
    font=("Arial", 15, "bold"),
    bg="#FFF4F7",
    wraplength=500
)

label_progression = tk.Label(
    window,
    text="",
    font=("Arial", 11, "bold"),
    bg="#FFF4F7"
)

label_score = tk.Label(
    window,
    text="Score : 0",
    font=("Arial", 11, "bold"),
    bg="#FFF4F7"
)

label_feedback = tk.Label(
    window,
    text="",
    font=("Arial", 12, "bold"),
    bg="#FFF4F7"
)

label_question.pack(pady=25)

bouton1 = tk.Button(
    window,
    text="",
    font=("Arial", 11),
    width=40
)
bouton1.pack(pady=5)

bouton2 = tk.Button(window, text="", font=("Arial", 11), width=40)
bouton2.pack(pady=5)

bouton3 = tk.Button(window, text="", font=("Arial", 11), width=40)
bouton3.pack(pady=5)

bouton4 = tk.Button(window, text="", font=("Arial", 11), width=40)
bouton4.pack(pady=5)

label_niveau.pack_forget()

btn_facile.pack_forget()
btn_difficile.pack_forget()
btn_tres_difficile.pack_forget()

label_question.pack_forget()

bouton1.pack_forget()
bouton2.pack_forget()
bouton3.pack_forget()
bouton4.pack_forget()

def Afficher_question(numero) :   
    question = questions[numero]
    label_question.config(text=question["QUESTION"])
    label_progression.config(text=f"Question {numero + 1} / {nombre_questions}")
    bouton1.config(text=question["OPTION"][0])
    bouton2.config(text=question["OPTION"][1])
    bouton3.config(text=question["OPTION"][2])
    bouton4.config(text=question["OPTION"][3]) 
  

def verifier_reponse(resultat) :
    global bonnes_reponses, mauvaises_reponses

    if resultat == questions[numero]["REPONSE"] :

       label_feedback.config(
           text="Youpiiii vous avez réussi !",
           fg="green"
       )
       bonnes_reponses += 1
       Gestion_score(True)

    else :
        label_feedback.config(
            text="Oups, vous avez échoué !",
            fg="red"
        )
        mauvaises_reponses += 1
        Gestion_score(False)
    
    window.after(1000, question_suivante)  
 


def Gestion_score(resultat_verification) :
    global score 
    
    if resultat_verification :
        score += 1
    label_score.config(text=f"Score : {score}")

bouton1.config(command=lambda: verifier_reponse(bouton1["text"]))
bouton2.config(command=lambda: verifier_reponse(bouton2["text"]))
bouton3.config(command=lambda: verifier_reponse(bouton3["text"]))
bouton4.config(command=lambda: verifier_reponse(bouton4["text"]))

window.mainloop()