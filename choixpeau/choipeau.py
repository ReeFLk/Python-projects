import csv
from functools import partial
from re import I
from turtle import width
import pygame
import sys


def extractionDonnees(nomFichier, separateur):
    '''
    précondition : nomFichier est du type str et doit être le nom d'un fichier csv.
                   separateur est de type str et doit être soit une virgule ou un point virgule.
    postcondition: Cette fonction récupère les données d'un fichier csv et renvoie un tableau contenant
    des dictionnaires dont les clés sont les descripteurs associés :
    La liste des descripteurs et la liste de toutes les données
    '''
    if nomFichier[-4:] != ".csv":
        return "Erreur : Ce fichier n'est pas un fichier CSV"
    else:
        tab = []
        with open('choixpeau/'+nomFichier, newline='', encoding='utf-8-sig') as csvfile:
            fichier = csv.DictReader(csvfile, delimiter=separateur)
    # pour remplir notre tableau, une boucle for parcourant chaque ligne du fichier csv sera utilisée
            for ligne in fichier:
                tab.append(dict(ligne))
        return tab


def characteristiques_rangement():
    characters_tab = extractionDonnees("Caracteristiques_des_persos.csv", ";")
    characteristiques = [character for character in characters_tab]
    return characteristiques


def characters_rangement():
    characters_tab = extractionDonnees("Characters.csv", ";")
    characters = [character for character in characters_tab]
    return characters


def distance(eleve1, eleve2):
    for eleve in characteristiques_rangement():
        if eleve['Name'] == eleve1:
            eleve1_info = eleve
        elif eleve['Name'] == eleve2['Name']:
            eleve2_info = eleve
        else:
            eleve2_info = eleve2
    return abs(int(eleve1_info['Courage'])-int(eleve2_info['Courage']))+abs(int(eleve1_info['Ambition'])-int(eleve2_info['Ambition']))+abs(int(eleve1_info['Intelligence'])-int(eleve2_info['Intelligence']))+abs(int(eleve1_info['Good'])-int(eleve2_info['Good']))


def knn_new_student(tab, new_eleve):
    ecart = [(eleve['Name'], distance(eleve['Name'], new_eleve))
             for eleve in tab]
    return sorted(ecart, key=lambda eleve: eleve[1])[:5]


def frequence_des_maisons(table):
    """ Précondition : table est une liste (ou un dictionnaire) d'élèves dans laquelle chaque est modélisé par un dictionnaire
    Postcondition : Un dictionnaire dont les clés sont les maisons et les valeurs leur effectif.
    """
    Gryffindor = 0
    Hufflepuff = 0
    Ravenclaw = 0
    Slytherin = 0
    for eleve in characters_rangement():
        for i in range(5):
            if eleve['House'] == "Gryffindor" and eleve['Name'] == table[i][0]:
                Gryffindor += 1
                break
            elif eleve['House'] == "Hufflepuff" and eleve['Name'] == table[i][0]:
                Hufflepuff += 1
                break
            elif eleve['House'] == "Ravenclaw" and eleve['Name'] == table[i][0]:
                Ravenclaw += 1
                break
            elif eleve['House'] == "Slytherin" and eleve['Name'] == table[i][0]:
                Slytherin += 1
                break
    if Gryffindor > Hufflepuff and Gryffindor > Ravenclaw and Gryffindor > Slytherin:
        return "Gryffindor"
    if Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
        return "Hufflepuff"
    if Ravenclaw > Hufflepuff and Ravenclaw > Gryffindor and Ravenclaw > Slytherin:
        return "Ravenclaw"
    if Slytherin > Hufflepuff and Slytherin > Ravenclaw and Slytherin > Gryffindor:
        return "Slytherin"


def qcm():
    global sentences, reponses
    sentences = []
    reponses = []
    with open("choixpeau/qcm.txt", 'r', newline='', encoding='utf-8-sig') as txtfile:
        for ligne in txtfile:
            ligne = ligne.replace("\n", "")
            sentences.append(ligne.split(" ? "))

    for i in range(len(sentences)):
        reponses.append(sentences[i].pop().split(";;"))


def create_tab_reponses():
    global tab_reponses
    tab_reponses = []
    for reponse in reponses:
        tab_reponses.append(reponse[1])
    print(tab_reponses)


def verification():
    global score
    if input_reponses[index_questions] == tab_reponses[index_questions]:
        score+=1

WIDTH = 1080
HEIGHT = 600

score = 0
input_reponses = []
qcm()
create_tab_reponses()


pygame.init()

wd = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Choipeau")
choipeau = pygame.image.load("choixpeau\sortinghat.png")
pygame.display.set_icon(choipeau)
clock = pygame.time.Clock()

input_text = ""
index_questions = 0

fantastic_font = pygame.font.Font("choixpeau/HARRYP__.TTF", 24)
base_font = pygame.font.Font(None, 24)

input_surface = fantastic_font.render(input_text, False, (255, 255, 255))
question_surface = fantastic_font.render(
    sentences[index_questions][0].upper() + "?", False, (255, 255, 255))
reponse_surface = fantastic_font.render(
    reponses[0][index_questions], False, (255, 255, 255))
question_rect = question_surface.get_rect(center=(WIDTH//2, 10))
reponse_rect = reponse_surface.get_rect(center=(WIDTH//2, 40))
input_text_rect = input_surface.get_rect(center=(WIDTH//2, 70))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                input_reponses.append(input_text)
                verification()
                index_questions += 1
                input_text = ""
                print(input_reponses , score )
                
            else:
                input_text += event.unicode.upper()

    wd.fill((0, 0, 0))
    input_surface = fantastic_font.render(input_text, False, (255, 255, 255))
    question_surface = fantastic_font.render(
        sentences[index_questions][0].upper() + "?", False, (255, 255, 255))
    reponse_surface = fantastic_font.render(
        reponses[index_questions][0], False, (255, 255, 255))
    question_rect = question_surface.get_rect(center=(WIDTH//2, 10))
    reponse_rect = reponse_surface.get_rect(center=(WIDTH//2, 40))
    wd.blit(question_surface, question_rect)
    wd.blit(reponse_surface, reponse_rect)
    wd.blit(input_surface, input_text_rect)
    pygame.display.update()
    clock.tick(30)


choix_final = frequence_des_maisons(knn_new_student(characteristiques_rangement(), {
                                    'Name': 'Draco Malfoy', 'Courage': '2', 'Ambition': '9', 'Intelligence': '8', 'Good': '4'}))
