from settings import *
from main import *

class Menu:
	def __init__(self, app):
		self.app = app
		self.font = pg.font.Font(font_i , size_font)
		self.text_rect = pg.Rect(40, 200, 190, 50)
		self.background = pg.transform.scale(pg.image.load('maxresdefault.jpg'), (W*TILE*1.2, H*TILE))
		self.result = 'true'

	def draw(self):
		self.app.screen.blit(self.background, (-10, 0))
		[draw_text(self.app.screen, "New game", self.text_rect, RED, font_i, size_font) if self.text_rect.colliderect(self.app.mouse_rect) else draw_text(self.app.screen, "New game", self.text_rect, BLACK, font_i, size_font)]

	def update(self):
		self.app.posititon_mouse = pg.mouse.get_pos()
		self.app.mouse_rect = pg.Rect(self.app.posititon_mouse[0], self.app.posititon_mouse[1], 1, 1)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit()
			if event.type == pg.MOUSEBUTTONDOWN and self.text_rect.colliderect(self.app.mouse_rect):
				if event.button == 1:
					self.result = 'false'

		pg.display.update()

	def run(self):
		while True:
			self.app.clock.tick(FPS)
			pg.display.set_caption(f'FPS: {self.app.clock.get_fps() :.2f}')
			self.draw()
			self.update()
			if self.result == 'false':
				self.result = 'true'
				break
