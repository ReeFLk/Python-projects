class Joueur:

    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def __str__(self):  # dunder
        return f"{self.nom}"

    def donne_main(self, deck, n):
        self.main = deck.donne_carte(n)

    def pose_carte(self, carte):
        self.main.remove(carte)

    def ramasse_carte(self, liste_cartes):
        self.main.extend(liste_cartes)
