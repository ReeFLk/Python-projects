import csv
from functools import partial
from operator import index
import pygame
import sys


def characteristiques_rangement():
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
    global characteristiques, characters
    characters_tab = extractionDonnees("Caracteristiques_des_persos.csv", ";")
    characteristiques = [character for character in characters_tab]
    characters_tab = extractionDonnees("Characters.csv", ";")
    characters = [character for character in characters_tab]


def knn_new_student(tab, new_eleve):
    def distance(eleve1, eleve2):
        for eleve in characteristiques_rangement():
            if eleve['Name'] == eleve1:
                eleve1_info = eleve
            elif eleve['Name'] == eleve2['Name']:
                eleve2_info = eleve
            else:
                eleve2_info = eleve2
        return abs(int(eleve1_info['Courage'])-int(eleve2_info['Courage']))+abs(int(eleve1_info['Ambition'])-int(eleve2_info['Ambition']))+abs(int(eleve1_info['Intelligence'])-int(eleve2_info['Intelligence']))+abs(int(eleve1_info['Good'])-int(eleve2_info['Good']))

    ecart = [(eleve['Name'], distance(eleve['Name'], new_eleve))
             for eleve in tab]
    return sorted(ecart, key=lambda eleve: eleve[1])[:5]


def qcm_intelligence():
    global sentences_qcm, reponses_qcm
    sentences_qcm = []
    reponses_qcm = []
    with open("choixpeau/qcm.txt", 'r', newline='', encoding='utf-8-sig') as txtfile:
        for ligne in txtfile:
            ligne = ligne.replace("\n", "")
            sentences_qcm.append(ligne.split(" ? "))

    for i in range(len(sentences_qcm)):
        reponses_qcm.append(sentences_qcm[i].pop().split(";;"))


def create_tab_reponses_qcm():
    global tab_reponses_qcm
    tab_reponses_qcm = []
    for reponse in reponses_qcm:
        tab_reponses_qcm.append(reponse[1])
    print(tab_reponses_qcm)


def verification():
    global score
    if input_reponses[index_questions] == tab_reponses_qcm[index_questions]:
        score += 1


def window_intelligence():
    input_surface = fantastic_font.render(input_text, False, (255, 255, 255))
    question_surface = fantastic_font.render(
        sentences_qcm_poudlard[index_questions][0].upper() + "?", False, (255, 255, 255))
    reponse_surface = fantastic_font.render(
        sentences_qcm_poudlard[index_questions][1], False, (255, 255, 255))
    question_rect = question_surface.get_rect(center=(WIDTH//2, 15))
    reponse_rect = reponse_surface.get_rect(center=(WIDTH//2, 45))
    wd.blit(question_surface, question_rect)
    wd.blit(reponse_surface, reponse_rect)
    wd.blit(input_surface, input_text_rect)


def qcm_poudlard():
    global sentences_qcm_poudlard
    sentences_qcm_poudlard = []
    with open("choixpeau/question_poudlard.txt", 'r', newline='', encoding='utf-8-sig') as txtfile:
        for ligne in txtfile:
            ligne = ligne.replace("\r", "").replace("\n", "")
            sentences_qcm_poudlard.append(ligne.split(" ? "))


def houses(tab):
    houses={}
    for e in tab:
        match e:
            case "A":
                if houses.get("Griffondor") is None:
                    houses["Griffondor"]=1
                houses["Griffondor"]+=1
            case "B":
                if houses.get("Serpentard")is None:
                    houses["Serpentard"]=1
                houses["Serpentard"]+=1
            case "C":
                if houses.get("Pouffessoufle")is None:
                    houses["Pouffessoufle"]=1
                houses["Pouffessoufle"]+=1
            case "D":
                if houses.get("Serdaigle")is None:
                    houses["Serdaigle"]=1
                houses["Serdaigle"]+=1
    return list(houses.items())
    

def window_houses():
    fantastic_font = pygame.font.Font("choixpeau/HARRYP__.TTF", 120)
    annonce_surface = fantastic_font.render(
        house[0][0], False, (255, 255, 255))
    annonce_rect = question_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    wd.blit(annonce_surface, annonce_rect)

WIDTH = 1080
HEIGHT = 600

score = 0
input_reponses = []
qcm_intelligence()
qcm_poudlard()


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
    sentences_qcm_poudlard[index_questions][0].upper() + "?", False, (255, 255, 255))
reponse_surface = fantastic_font.render(
    sentences_qcm_poudlard[index_questions][1], False, (255, 255, 255))
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
                # verification()
                if index_questions >= 25:
                    break
                    index_questions = 0
                index_questions += 1
                input_text = ""
            else:
                input_text += event.unicode.upper()

    wd.fill((0, 0, 0))
    if index_questions < 25:
        window_intelligence()
    else:
        house=houses(input_reponses)
        window_houses()
    pygame.display.update()
    clock.tick(30)
