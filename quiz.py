from tkinter import *
import math
from random import *
from functools import partial
from time import *
import os

#Variables Globales

level = 0
list_length = 3
random_i = randint(0, list_length - 1)
start = None
end = None

#Données : Questions et bonnes réponses

questions = [
    #Questions Niveau 0
    ['Qui est le président de la France ? a.Macron  b.Sarkozy  c.Hollande', #1er parcours
    'Quelle est la capitale de la France ? a.Lyon b.Paris c.Marseille',#2ème parcours
    'Quel est le triple de 30 ? a.60  b.33  c.90'],#3ème parcours
    #Nivau 1
   ["Avec quel légume fait-on les frites ? a.des carottes   b.des pommes de terre  c.des courgettes",
    "Quel insecte produit le miel ? a.Le puceron b.Le scarabée c.L’abeille ", 
    "Qui est ce youtuber ? a.Squeezie b.Norman c.Cyprien "],
    #Nivau 2
    ["Qui est ce personnage ? a.Krilin b.Son Goku c.Vegeta", 
    "Qui a remporté le plus de ballon d'or ? a.Ronaldo b.Messi c.Zidane", 
    "De quel pays appartient ce drapeau ? a.Pologne b.L’Indonésie c.Monaco"],
    #Nivau 3
    ["Quelle est la première ville du monde à s’être dotée d’un métro ? a.Paris b.Londres c.New York ",
    "Quel est le jeu vidéo le plus vendu au monde ? a.GTA b.Tetris c.Minecraft",
    "Qui est l’homme le plus riche du monde en 2021 ? a.Jeff Bezos b.Bill Gates c.Elon Musk"],
    #Nivau 4
    ["Quel est le langage de programmation le plus utilisé dans le monde ? a.Java b.Python c.JavaScript",
    "Qui est le joueur de NBA ayant inscrit le plus de points durant un match ? a.Wilt Chamberlain b.Michael Jordan c.Lebron James",
    "Qui a gagné l’oscar du meilleur acteur en 2016 ? a.Brad Pitt b.Joaquin Phoenix c.Leonardo Dicaprio"],
    #Nivau 5
    ["Qui est ce rappeur ? a.Playboi carti b.Lil uzi vert c.Dababy",
    "Quel est le plus long fleuve du monde? a.Le Nil b.La Seine c.L'Amazone",
    "Le corps humain est composé à combien de pourcentage d’eau? a.65  b.67 c.66",],
    #Nivau 6
    ["Qui a rendu la langue française officielle dans l’administration française ? a.François Ier b.Napoléon Bonaparte c.Charlemagne",
    "Combien de nos jours, vaut un Bitcoin en euros (approximativement) a.146 000 € b.12 000 € c.54 000  €",
    "Ce tableau représente quel événement ? a.La grande révolution française b.Les Trois Glorieuses c.Massacre de Saint Barthélémy" ],
    #Nivau 7
    ["Quand la météorite qui a causé l'extinction des dinosaures est-elle tombée sur Terre ? a.65 millions d années b.112 300 millions d'années c.100 millions d années",
    'Qui est ce dieu de la mythologie grecque ? a.Hadès b.Arès c.Hermès',
    'Quelle est l’écriture correcte du nom de cet animal ? a.Ornithorynque b.Ornythorinque c.Ornitorynque'],

    ["", "", ""]#Liste laissée vide volontairement, ne pas toucher

    ]

correct_answers = [
    #Réponses correctes des questions du niveau 0
    ['a', 'b', 'c'],
    #Niveau 1
    ['b', 'c', 'a'],
    #Niveau 2
    ['c', 'b', 'a'],
    #Niveau 3
    ['b', 'c', 'c'],
    #Niveau 4
    ['c', 'a', 'c'],
    #Niveau 5
    ['b', 'a', 'c'],
    #Niveau 6
    ['a', 'c', 'b'],
    #Niveau 7
    ['a', 'b', 'a']
    ]

#Structure de l'interface

#Paramètres
app = Tk()
app.title('Quiz')
app.geometry("1080x720")
app.config(bg='white')
app.iconbitmap('images/question-icon.ico')

#Composants
label_title = Label(app, text="Quiz", font=('Calibri',45), bg='white')

label_level = Label(app, text=("Niveau", level), font=('Calibri',25), bg='white', fg="#FF625A")


label_question = Label(app, text="", font=('Calibri', 22), height=3, bg='white')


answers_frame = Frame(app, width=4, bg="white")


all_answers = [
                Button(answers_frame, text="a", font=('Calibri', 30), height=1, width=4, bg="#ff625a", fg="white"),
                Button(answers_frame, text="b", font=('Calibri', 30), height=1, width=4, bg="#ff625a", fg="white"), 
                Button(answers_frame, text="c", font=('Calibri', 30), height=1, width=4, bg="#ff625a", fg="white")
                ]

space_between_buttons = 25

label_result = Label(app, text="", font=('Arial', 25), bg='white',)

canvas_width = 350
canvas_height = 350

question_image = PhotoImage(file="images/question_mark.png")
canvas = Canvas(app, width=canvas_width, height=canvas_height, bg='white', bd=0, highlightthickness=0)
canvas.create_image(canvas_width/2, canvas_height/2, image=question_image)

label_game_over = Label(app, text="Vous avez échouer, voulez vous rejouer ?", font=('Arial', 25), bg='white')
yes_btn = Button(app, text="Oui", font=('Calibri', 30), height=1, width=4, bg="#ff625a", fg="white")
no_btn = Button(app, text="Non", font=('Calibri', 30), height=1, width=4, bg="#ff625a", fg="white")

label_victory = Label(app, text="", font=('Arial', 25), bg='white')

#Fonctions

def change_image(image):
    """
    Change le fichier d'un composant PhotoImage en fonction d'une question
    image : image qui va etre changée
    """
    if label_question['text'] == questions[0][2]:
        image['file'] = "images/squeezie.png"
    elif label_question['text'] == questions[1][2]:
        image['file'] = "images/pologne.png"
    elif label_question['text'] == questions[1][0]:
        image['file'] = "images/vegeta.png"
    elif label_question["text"] == questions[4][0]:
        image['file'] = "images/lil_uzi_vert.png"
    elif label_question["text"] == questions[5][2]:
        image['file'] = "images/tableau.png"
    elif label_question["text"] == questions[6][1]:
        image['file'] = "images/Ares.png"
    else:
        image["file"] = "images/question_mark.png"


def generate_question(question):
    '''
    génére aléatoirement une question parmi une liste et l'affiche
    question : (str) liste dans laquelle une question va etre générée aléatoirement
    return : (str) retourne une question choisie aléatoirement dans une liste
    '''
    random_question = question[random_i]
    label_question["text"] = random_question
    return random_question

def leave_game():
    """
    Ferme l'application
    """
    app.destroy()

def right_answer():
    """
    Change le texte de label_result par "Bonne réponse", et sa couleur de texte par '#77D353',
    incrémente level et i de 1, change le texte de label_level par "Niveau", level et retourne True
    return (bool) Retourne True
    """
    global level
    label_result["text"] = "Bonne réponse"
    label_result["fg"] =  '#77D353'
    level += 1
    label_level["text"] = "Niveau", level
    return True

def wrong_answer():
    """
    Supprime tout les composants visibles et Affiche les composants à afficher en cas de mauvaise réponse
    """
    canvas.pack_forget() 
    label_title.pack_forget() 
    label_result.pack_forget() 
    label_level.pack_forget() 
    label_question.pack_forget() 
    for answer in all_answers:
        answer.grid_forget() 
    label_game_over.pack()
    yes_btn.pack(expand=YES)
    no_btn.pack(expand=YES)

def win_game():
    """
    Supprime tout les composants actuels de l'application et affiche les composants à afficher en cas de victoire
    """
    canvas.pack_forget() 
    label_title.pack_forget() 
    label_result.pack_forget() 
    label_level.pack_forget() 
    label_question.pack_forget() 
    for answer in all_answers:
         answer.grid_forget()
    label_victory.pack()
    yes_btn.pack(expand=YES)
    no_btn.pack(expand=YES)
    end = time()#end prend la valeur de l'heure actuelle en secondes (donc end > start)
    time_elapsed = end - start
    label_victory['text'] = "Bravo vous avez fini le quiz en {} secondes, voulez vous rejouer ?".format(math.ceil(time_elapsed))

def check_answer(button):
    """
    Vérifie si la bonne réponse correspond au texte du bouton cliqué et appelle right_answer(), change_image et generate_question() sinon appelle wrong_answer()
    et si lorsqu'on clique sur la bonne réponse et qu'on atteint le niveau max, appelle win_game()
    button : (tkinter.Button) Bouton sur lequel on va vérifier le texte
    """
    if correct_answers[level][random_i] == button['text']:
        right_answer()
        change_image(question_image)
        generate_question(questions[level])
    else:
        wrong_answer()

    if level == 8:
        win_game()
        

def new_game():
    """
    Lance une nouvelle partie, affichage des composants nécessaires pour jouer
    """
    global start
    global end
    start = time()#start prend la valeur de l'heure actuelle en secondes
    label_title.pack()
    label_level.pack()
    label_question.pack()
    answers_frame.pack(expand=YES)
    all_answers[0].grid(row=0, column=1, padx=space_between_buttons)
    all_answers[1].grid(row=0, column=2, padx=space_between_buttons)
    all_answers[2].grid(row=0, column=3, padx=space_between_buttons)
    label_result.pack()
    canvas.pack()
    global level
    global i
    generate_question(questions[level])
    for answer in all_answers:
        answer['command'] = partial(check_answer, answer)
new_game()

def play_again():
    """
    Ferme l'application puis la réouvre
    """
    app.destroy()
    os.startfile("quiz.py")

no_btn["command"] = leave_game

yes_btn["command"] = play_again


app.mainloop()
