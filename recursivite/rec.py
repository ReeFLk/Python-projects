from turtle import *
couleurs=['blue', 'green', 'yellow', 'orange', 'red', 'purple']

bgcolor('black')

def dessin():
    for i in range(180):
        color(couleurs[i%6])
        forward(i)
        right(59)


def dessin_rec(i):
    if i<180:
        color(couleurs[i%6])
        forward(i)
        right(59)
        dessin_rec(i+1)
    else: return 1


dessin_rec(0)

