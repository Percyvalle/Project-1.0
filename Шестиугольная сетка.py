import numpy as np
import pygame as pg
import random

from settings import *


W, H = 30, 25
TILE = 30
i_W, i_H = 120, 140

class App:
    def __init__(self):
        self.res = self.width, self.height = (W*TILE, H*TILE)
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.gete = []
        #for y in range(-1, H):
        #    for x in range(-1, W):
        #        if y%2 == 0:
        #            self.gete.append(pg.Rect(x*(i_W//2)+30, y*(i_H//3), i_W//2, i_H//2))
        #        else:
        #            self.gete.append(pg.Rect(x*(i_W//2), y*(i_H//3), i_W//2, i_H//2))
        self.gete = [pg.Rect(x*(i_W//2)+30, y*(i_H//3), i_W//2, i_H//2) if y%2 == 0 else pg.Rect(x*(i_W//2), y*(i_H//3), i_W//2, i_H//2) for x in range(-1, W) for y in range(-1, H)]
        self.image_1 = [pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_06.png").convert_alpha(), (i_W//2, i_H//2)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_11.png").convert_alpha(), (i_W//2, i_H//2)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_03.png").convert_alpha(), (i_W//2, i_H//2)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_02.png").convert_alpha(), (i_W//2, i_H//2)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_11.png").convert_alpha(), (i_W//2, i_H//2))]
        self.arr_sur = [random.randint(0, 1) for x in range(806)]

    def draw(self):   
        [self.screen.blit(self.image_1[self.arr_sur[val]], i_rect) for val,i_rect in enumerate(self.gete)]

    def update(self):
        pg.display.update()

    def run(self):
        while True:
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(FPS)
            pg.display.set_caption(f'FPS: {self.clock.get_fps() :.2f}')
            self.draw()
            self.update()

if __name__ == '__main__':
    app = App()
    app.run()