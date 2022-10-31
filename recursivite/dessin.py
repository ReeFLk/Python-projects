from PIL import Image
from guizero import *
import sys

sys.setrecursionlimit(10**9)


def clicked(event_data):
    coloriage(int(event_data.x), int(event_data.y))
    picture.image = i


def coloriage(x, y):
    if 0 < y < height and 0 < x < width:
        if i.getpixel((x, y))[0] > 180 and i.getpixel((x, y))[1] > 180 and i.getpixel((x, y))[2] > 180:
            i.putpixel((x, y), color_choice)
            coloriage(x, y+1)
            coloriage(x, y-1)
            coloriage(x+1, y)
            coloriage(x-1, y)
    else:
        return 0


def color(c):
    global color_choice
    match c:
        case 1:
            color_choice = (255, 255, 0, 255)
        case 2:
            color_choice = (255, 0, 0)
        case 3:
            color_choice = (0, 255, 0)
        case 4:
            color_choice = (212, 115, 212)


i = Image.open("recursivite/canard.png").convert('RGB')
width, height = i.size


app = App()
picture = Picture(app, image=i)
yellow_button = PushButton(app, text="Jaune", command=color, args=[1])
rouge_button = PushButton(app, text="Rouge", command=color, args=[2])
vert_button = PushButton(app, text="Vert", command=color, args=[3])
purple_button = PushButton(app, text="purple", command=color, args=[4])
picture.when_clicked = clicked

app.display()
