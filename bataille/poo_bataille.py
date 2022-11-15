from joueur import Joueur
from deck import Deck


class Bataille:

    def __init__(self, nb_joueurs):
        self.nb_joueurs = nb_joueurs
        self.liste_joueurs = self.players()

    def players(self):

        joueurs = []
        for i in range(self.nb_joueurs):
            nom = input(f"Veuillez rentrer le nom de joueur {i+1} : \n")
            joueurs.append(Joueur(nom))
        return joueurs

    def start(self):
        paquet = Deck()
        paquet.melange()
        nb_carte = len(paquet)//2
        for joueur in self.liste_joueurs:
            joueur.donne_main(paquet, nb_carte)
        self.bataille()

    def bataille(self):
        j1 = self.liste_joueurs[0]
        j2 = self.liste_joueurs[1]
        while len(j1.main) > 0 and len(j2.main) > 0:
            pile = []
            gagnant, pli = self.pli(pile)
            if gagnant == 0:
                print("Egalite l'un des joueurs n'a plus de cartes")
                return 0
            gagnant.ramasse_carte(pli)
        print("\nLa partie est terminée\n")
        if len(j2.main) > len(j2.main):
            print(f"{j2} gagne!")
        else:
            print(f"{j1} gagne!")
        return 0

    def pli(self, pile):
        j1 = self.liste_joueurs[0]
        j2 = self.liste_joueurs[1]
        carte_1 = j1.main[0]
        carte_2 = j2.main[0]
        pile.append(carte_1)
        pile.append(carte_2)
        print(f"{self.liste_joueurs[0].nom} pose la carte {carte_1}")
        self.liste_joueurs[0].pose_carte(self.liste_joueurs[0].main[0])
        print(f"{self.liste_joueurs[1].nom} pose la carte {carte_2}")
        self.liste_joueurs[1].pose_carte(self.liste_joueurs[1].main[0])
        print(f"{carte_1} VS {carte_2}")
        if carte_1 > carte_2:
            print(f"{carte_1} est plus forte, c'est {j1} qui gagne le pli")
            gagnant = j1
        elif carte_1 == carte_2 and len(j2.main) > 0:
            print("égalité")
            self.pli(pile)
            gagnant = j1
        elif len(j2.main) <= 0:
            return 0, pile
        else:
            print(f"{carte_2} est plus forte, c'est {j2} qui gagne le pli")
            gagnant = j2
        return gagnant, pile


partie = Bataille(2)
print(partie)
partie.start()
