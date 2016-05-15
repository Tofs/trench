import pygame
import sys
import constants
from pygame.locals import *


pygame.init()
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption("hello world!")

rect = pygame.rect.Rect(10,10,10,10)

while True:
	window.fill(constants.BLACK)
	window.blit(rect, 10, 10)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
