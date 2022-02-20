import numpy as np
import pygame as pg
import sys
import random

from settings import *
from menu import *

pg.font.init()
class App:
    def __init__(self):
        self.res = self.width, self.height = (W*TILE, H*TILE)
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.posititon_mouse = pg.mouse.get_pos()
        self.mouse_rect = pg.Rect(self.posititon_mouse[0], self.posititon_mouse[1], 1, 1)
        self.menu = Menu(self)
        self.gete = [pg.Rect(x*i_W+30, y*(i_H//1.5)+150, i_W, i_H) if y%2 == 0 else pg.Rect(x*(i_W), y*(i_H//1.5)+150, i_W, i_H) for x in range(-1, W) for y in range(-1, H)]
        self.arr_sur = [random.randint(0, number_of_cells) for x in range(806)]
        self.image_1 = [pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_06.png").convert_alpha(), (i_W, i_H)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_11.png").convert_alpha(), (i_W, i_H)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_03.png").convert_alpha(), (i_W, i_H)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_02.png").convert_alpha(), (i_W, i_H)),
                        pg.transform.scale(pg.image.load("Terrain/Dirt/dirt_11.png").convert_alpha(), (i_W, i_H))]

    def draw(self):   
        [self.screen.blit(self.image_1[3], i_rect) if self.mouse_rect.colliderect(i_rect) else self.screen.blit(self.image_1[self.arr_sur[val]], i_rect) for val,i_rect in enumerate(self.gete)]

    def update(self):
        self.posititon_mouse = pg.mouse.get_pos()
        self.mouse_rect = pg.Rect(self.posititon_mouse[0], self.posititon_mouse[1], 1, 1)

        pg.display.update()

    def run(self):
        self.menu.run()
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()
                if i.type == pg.KEYDOWN:
                    if i.key == pg.K_q:
                        self.menu.run()
                    if i.key == pg.K_LEFT:
                        for i in self.gete:
                            i.y += 10
            self.clock.tick(FPS)
            pg.display.set_caption(f'FPS: {self.clock.get_fps() :.2f}')
            self.draw()
            self.update()

if __name__ == '__main__':
    app = App()
    app.run()