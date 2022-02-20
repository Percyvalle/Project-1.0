import numpy as np
import random
import pygame as pg

from settings import *


W, H = 10, 20
TILE = 30


class App:
    def __init__(self):
        self.res = self.width, self.height = (W*TILE, H*TILE)
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.gete = [pg.Rect(x*TILE, y*TILE, TILE, TILE) for x in range(W) for y in range(H)]

    def draw(self):
        [pg.draw.rect(self.screen, (40,40,40), i_rect, 1) for i_rect in self.gete]

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