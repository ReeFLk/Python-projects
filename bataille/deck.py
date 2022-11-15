from carte import Carte
from random import shuffle


class Deck:

    def __init__(self):
        self.cartes = []
        self.couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
        self.noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        self.build()

    def build(self):
        self.cartes = [Carte(c, n) for c in self.couleurs
                    for n in self.noms]

    def __len__(self):
        return len(self.cartes)

    def melange(self):
        shuffle(self.cartes)

    def donne_carte(self, n):
        return [self.cartes.pop() for _ in range(n)]
