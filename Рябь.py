import numpy as np
import random
import pygame as pg

from settings import *


W, H = 25, 25
TILE = 30


class App:
    def __init__(self):
        self.res = self.width, self.height = (W*TILE, H*TILE)
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.array_f = np.full((W*TILE, H*TILE, 3), [0, 0, 0])

    def draw(self):
        self.screen.blit(pg.surfarray.make_surface(self.array_f), (0, 0))
    
    def update(self):
        self.array_f = np.random.randint(0, 255, size=self.array_f.shape)
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