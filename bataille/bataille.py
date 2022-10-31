import random
class Carte():
    def __init__(self, couleur, nom):
        self.couleur = couleur
        self.nom = nom
        self.carte = [self.couleur, self.nom]
    
    def getCarte(self):
        return self.carte

class Jeu():
    def __init__(self):
        self.cartes = []
        self.couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
        self.noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        self.valeurs = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Valet':11, 'Dame':12, 'Roi':13, 'As':14 }
        self.j1 = []
        self.j2 = []
        self.liste_en_cours=[] 
        for couleur in self.couleurs:
            for nom in self.noms:
                self.cartes.append(Carte(couleur, nom).getCarte())
    def getCartes(self):
        print(self.cartes)
        return self.cartes

    def getCartesMelange(self):
        random.shuffle(self.cartes)
        return self.cartes

    def distribution(self):
        for i in range(len(self.getCartesMelange())):
            if i%2==0:
                self.j1.append(self.cartes[i])
            else:
                self.j2.append(self.cartes[i])
        # print(str(len(self.j1))+"\n"+ str(len(self.j2)))
        return self.j1, self.j2

    def partie(self):
        while len(self.j1) >= 1 and len(self.j2) >= 1:
            j1_en_cours = list(self.j1.pop())
            j2_en_cours = list(self.j2.pop())
            print(j1_en_cours, j2_en_cours)
            if self.valeurs[j1_en_cours[1]] > self.valeurs[j2_en_cours[1]]:
                self.j1.insert(0, j1_en_cours)
                self.j1.insert(0, j2_en_cours)
            elif self.valeurs[j1_en_cours[1]] < self.valeurs[j2_en_cours[1]]:
                self.j2.insert(0, j1_en_cours)
                self.j2.insert(0, j2_en_cours)
            else:
                print("HEY")
                fin_bataille = self.bataille(j1_en_cours, j2_en_cours)
                if fin_bataille == 1:
                    for carte in self.liste_en_cours:
                        self.j1.insert(0, carte)
                elif fin_bataille == 2:
                    for carte in self.liste_en_cours:
                        self.j2.insert(0, carte)
                else:
                    print('plus de carte')
                self.liste_en_cours.clear()
        print("GG au j" + str(fin_bataille))
    def bataille(self, j1_passe, j2_passe):
        self.liste_en_cours.append(j1_passe)
        self.liste_en_cours.append(j2_passe)
        print(self.liste_en_cours)
        while self.valeurs[j1_passe[1]] == self.valeurs[j2_passe[1]] and (len(self.j1) >= 1 and len(self.j2) >= 1):
            j1_en_cours = list(self.j1.pop())
            j2_en_cours = list(self.j2.pop())
            print(j1_en_cours, j2_en_cours)
            if self.valeurs[j1_en_cours[1]] > self.valeurs[j2_en_cours[1]]:
                self.liste_en_cours.insert(0, j1_en_cours)
                self.liste_en_cours.insert(0, j2_en_cours)
                print(self.liste_en_cours)
                return 1
            elif self.valeurs[j1_en_cours[1]] < self.valeurs[j2_en_cours[1]]:
                self.liste_en_cours.insert(0, j1_en_cours)
                self.liste_en_cours.insert(0, j2_en_cours)
                print(self.liste_en_cours)
                return 2
            else:
                    self.bataille(j1_en_cours, j2_en_cours)
        if len(self.j1) <= 0 or len(self.j2) <= 0:
            return 3

if __name__ == "__main__":
    jeu=Jeu()
    jeu.distribution()
    jeu.partie()