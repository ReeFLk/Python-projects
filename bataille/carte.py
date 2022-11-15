valeurs = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Valet':11, 'Dame':12, 'Roi':13, 'As':14 }

class Carte:

    def __init__(self, couleur, nom):
        self.couleur = couleur
        self.nom = nom
        self.valeur = valeurs[self.nom]
    
    def __str__(self):
        return f"{self.nom} {self.couleur}"

    def __lt__(self, other):
        if self.valeur < other.valeur:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.valeur > other.valeur:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.valeur == other.valeur:
            return True
        else:
            return False
