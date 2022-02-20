import pygame as pg
import numpy as np

def draw_text(screen, text, text_rect, color, font_f, size):
		font = pg.font.Font(font_f, size)
		text_menu = font.render(text, True, color)
		screen.blit(text_menu, text_rect)

#settings display
FPS = 120
W, H = 30, 25
TILE = 25
i_W, i_H = 60, 70
res = width, height = (W*TILE, H*TILE)

#settings font
size_font = 48
font_i = '19316.ttf'

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#settings maps
number_of_cells = 1