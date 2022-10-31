import pygame


class SpriteSheet:
    def __init__(self, file_name, cols, rows):
        self.sprite_sheet = pygame.image.load(file_name)
        self.width = self.sprite_sheet.get_width()//cols
        self.height = self.sprite_sheet.get_height()//rows
        self.cols = cols
        self.rows = rows
        self.length = cols * rows

    def get_image_by_index(self, n):
        ny = n // self.cols
        nx = n % self.cols

        x = nx * self.width
        y = ny * self.height

        return self.sprite_sheet.subsurface((x, y, self.width, self.height))

    def filmstrip(self, start=0, length=None):
        if length == None:
            length = self.length
        return [self.get_image_by_index(i) for i in range(start, start+length)]
