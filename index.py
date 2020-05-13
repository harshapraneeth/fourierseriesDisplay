import math
import time
import pygame as pg
from pygame import gfxdraw as gf

size = (1000, 800)
hsize = (size[0]//2, size[1]//2)
tlen = 1000 #trace length
tll = 1 #trace line length
n = 5


t, pp = 0, []
def ma(p): return (hsize[0]-200+p[0], hsize[1]-p[1])
def ma2(p): return (hsize[0]+100+p[0], hsize[1]-p[1])

def draw(screen):
    global t, pp
    screen.fill((0, 0, 0))
    x, y = 0, 0
    for i in range(n):
        px, py = x, y
        pn = 2*i+1
        r = round(100*(4/(pn*math.pi)))
        x = round(x+r*math.cos(pn*t))
        y = round(y+r*math.sin(pn*t))
        gf.circle(screen, ma((px,0))[0], ma((0,py))[1], r, (255,255,255,96))
        pg.draw.line(screen, (255,255,255), ma((px, py)), ma((x,y)), 1)
    pp = [y]+pp
    pg.draw.line(screen,(0,255,0), ma((x,y)), ma((200,pp[0])))
    trace()
    t += 0.05

def trace():
    global pp
    n = len(pp)
    if n>tlen: pp, n = pp[:tlen], tlen
    if n>tll:
        for i in range(n-tll):
            pg.draw.line(screen,(0,255,0),(hsize[0]+i,hsize[1]-pp[i]),(hsize[0]+i+tll,hsize[1]-pp[i+tll]),1)

pg.init()
screen = pg.display.set_mode(size, pg.SRCALPHA)
pg.display.set_caption('Fourier Draws')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: pg.quit()
    draw(screen)
    pg.display.update()
    time.sleep(0.01)
