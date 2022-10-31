import pyxel as pyx
from random import randint


class Jeu():

    def __init__(self):
        self.WIDTH = 128
        self.HEIGHT = 128
        pyx.init(self.WIDTH, self.HEIGHT, title="Space Invaders")
        pyx.load("pyxel_resource/image0")
        self.vie = 3
        self.score = 0
        self.x = 55
        self.y = 100
        self.tirs_list = []
        self.ennemis_list = []
        self.explosions_list = []
        pyx.run(self.update, self.draw)

    def update(self):
        if pyx.btnp(pyx.KEY_F12):
            pyx.quit()
        self.ennemis_creation()
        self.ennemis_deplacement()
        self.vaisseau_deplacement()
        self.tir_creation()
        self.tirs_deplacement()
        self.vaisseau_supression()
        self.ennemis_supression()

    def draw(self):
        pyx.cls(0)
        pyx.rect(self.x, self.y, 10, 10, 11)
        pyx.text(1, 1, f"Vie = {self.vie}", 1)
        pyx.text(1, 6, f"Score = {self.score}", 1)
        if len(self.tirs_list):
            for tir in self.tirs_list:
                pyx.rect(tir[0], tir[1], 2, 2, 3)
        if len(self.ennemis_list):
            for ennemi in self.ennemis_list:
                pyx.rect(ennemi[0], ennemi[1], 6, 6, 6)
        if len(self.explosions_list):
            for explo in self.explosions_list:
                pyx.cirb(explo[0], explo[1], 6, 9)

    def vaisseau_deplacement(self):
        if pyx.btnp(pyx.KEY_UP, True, True) and self.y > 0:
            self.y -= 2
        if pyx.btnp(pyx.KEY_LEFT, True, True) and self.x > 0:
            self.x -= 2
        if pyx.btnp(pyx.KEY_RIGHT, True, True) and self.x+10 < self.WIDTH:
            self.x += 2
        if pyx.btnp(pyx.KEY_DOWN, True, True) and self.y+10 < self.HEIGHT:
            self.y += 2
        else:
            self.y = pyx.mouse_y
            self.x = pyx.mouse_x

    def tir_creation(self):
        if (pyx.btnp(pyx.KEY_SPACE) or pyx.btnp(pyx.MOUSE_BUTTON_LEFT)) and len(self.tirs_list) < 8:
            self.tirs_list.append([self.x+4, self.y-2])

    def tirs_deplacement(self):
        for tir in self.tirs_list:
            tir[1] -= 1
            if tir[1] < -8:
                self.tirs_list.remove(tir)

    def ennemis_creation(self):
        if (randint(0, 100) % 44 == 0) and len(self.ennemis_list) < 6:
            self.ennemis_list.append([randint(0, 120), 0])

    def ennemis_deplacement(self):
        for ennemi in self.ennemis_list:
            ennemi[1] += 1
            if ennemi[1] > 135:
                self.ennemis_list.remove(ennemi)

    def vaisseau_supression(self):
        if len(self.ennemis_list):
            if self.vie <= 0:
                pyx.quit()
            for i in range(len(self.ennemis_list)):
                if (self.ennemis_list[i][0] <= self.x <= self.ennemis_list[i][0]+6 or self.ennemis_list[i][0] <= self.x+9 <= self.ennemis_list[i][0]+6) and (self.ennemis_list[i][1] <= self.y <= self.ennemis_list[i][1]+6 or self.ennemis_list[i][1] <= self.y+9 <= self.ennemis_list[i][1]+6):
                    self.vie -= 1
                    self.ennemis_list.remove(self.ennemis_list[i])
                    break

    def ennemis_supression(self):
        if len(self.ennemis_list) and len(self.tirs_list):
            for i in range(len(self.ennemis_list)):
                for j in range(len(self.tirs_list)):
                    if (self.ennemis_list[i][0] <= self.tirs_list[j][0] <= self.ennemis_list[i][0]+6 or self.ennemis_list[i][0] <= self.tirs_list[j][0]+2 <= self.ennemis_list[i][0]+6) and (self.ennemis_list[i][1] <= self.tirs_list[j][1] <= self.ennemis_list[i][1]+6 or self.ennemis_list[i][1] <= self.tirs_list[j][1] + 2 <= self.ennemis_list[i][1]+6):
                        self.ennemis_list.remove(self.ennemis_list[i])
                        self.score += 1
                        self.ennemis_list.append(self.ennemis_list[i])
                        return 0

    # def explosions_animation(self):
    #     for explosion in self.explosions_list:
    #         explosion[2] += 1
    #         if explosion[2] == 12:
    #             self.explosions_list.remove(explosion)


if __name__ == "__main__":
    Jeu()
