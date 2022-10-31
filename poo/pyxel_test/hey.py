import pyxel as pyx
class App:
    def __init__(self):
        pyx.init(160, 120)
        self.x = 0
        pyx.load("my_ressources.pyxres", True, False, False, False)
        pyx.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyx.width

    def draw(self):
        pyx.cls(0)
        pyx.blt(0,0 ,0, 16,0, 8, 8)

App()