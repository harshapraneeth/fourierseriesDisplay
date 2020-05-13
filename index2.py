import math
import time
import pygame as pg
from pygame import gfxdraw as gf
import numpy as np

drawing = [(x,100*(math.sin(x/10))) for x in np.arange(-100*math.pi,0,1)]
drawing += [(x,100*(math.sin(x/10))) for x in np.arange(0,100*math.pi,1)]
drawing += [(-x,-100*(math.sin(x/10))) for x in np.arange(-100*math.pi,0,1)]
drawing += [(-x,-100*(math.sin(x/10))) for x in np.arange(0,100*math.pi,1)]

def addc(p1, p2): return (p1[0]+p2[0], p1[1]+p2[1])
def mulc(p1, p2): return (p1[0]*p2[0]-p1[1]*p2[1], p1[0]*p2[1]+p1[1]*p2[0])
def move(p): return (p[0], p[1])

def dft(x):
    C, N = [], len(x)
    step = 1
    for k in range(0,N,step):
        s = (0,0)
        for n in range(0,N,step):
            phi = (2*math.pi*k*n)/N
            c = (math.cos(phi), math.sin(phi))
            s = addc(s, mulc(x[n],c))
        s = (s[0]*step/N, s[1]*step/N)
        C.append((s[0], s[1], k, math.sqrt(s[0]*s[0]+s[1]*s[1]), math.atan2(s[1],s[0])))
    return C

x, path = [], []
for i in drawing: x.append((i[0], i[1]))
t, fx = 0, dft(x)

def cycle(x, y, r, f):
    for i in range(len(f)):
        px, py = x, y
        fq, rd, ph = f[i][2], f[i][3], f[i][4]
        x += rd*math.cos(fq*t+ph+r)
        y += rd*math.sin(fq*t+ph+r)
        gf.circle(screen, round(move((px,0))[0]), round(move((0,py))[1]), round(rd), (255,255,255,98))
        pg.draw.line(screen, (255,255,255), move((px, py)), move((x,y)), 1)
    return (x,y)

def trace(pp):
    try:
        for i in range(1,len(pp)): pg.draw.line(screen, (0,255,0), move((round(pp[i-1][0]), round(pp[i-1][1]))), move((round(pp[i][0]), round(pp[i][1]))), 1)
    except: pass

pg.init()
screen = pg.display.set_mode((800,800))
pg.display.set_caption('Fourier Draws')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: pg.quit()
    screen.fill((0, 0, 0))
    path = [cycle(400, 400, 0, fx)]+path
    trace(path)
    dt = 2*math.pi/len(fx)
    t += dt
    if t> 4*math.pi: t, path = 0, []
    pg.display.update()
    #time.sleep(0.01)
