import pygame
import sys
from random import randint

#Параметры экрана
WIDTH = 425
HEIGHT = 600

#Переменные цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

while True:
	screen.fill(BLACK)
	
	rect1 = pygame.draw.rect(screen, WHITE, (WIDTH - 105, HEIGHT - 105, 100, 100))
	rect2 = pygame.draw.rect(screen, WHITE, (WIDTH - 105*2, HEIGHT - 105, 100, 100))
	rect3 = pygame.draw.rect(screen, WHITE, (WIDTH - 105*3, HEIGHT - 105, 100, 100))
	rect4 = pygame.draw.rect(screen, WHITE, (WIDTH - 105*4, HEIGHT - 105, 100, 100))

	pygame.display.flip()

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()

	

		




























# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (200, 200, 200)
# LIGHT_GRAY = (240, 240, 240)

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Calculator")



# x = 0
# y = 0
# x1 = 20
# y1 = 20
# clock = pygame.time.Clock()

# while True:
# 	screen.fill(BLACK)
# 	snake_pos = [100, 50] 
# 	pygame.draw.rect(screen, LIGHT_GRAY, (20, 20, 50, 50))
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 			sys.exit()
# 		if event.type == pygame.KEYDOWN:
# 			if event.key == pygame.K_ESCAPE:
# 				pygame.quit()
# 				sys.exit()

# 	keys = pygame.key.get_pressed()
	
# 	if keys[pygame.K_RIGHT]:
# 		x +=10
# 	if keys[pygame.K_LEFT]:
# 		x -=10
# 	if keys[pygame.K_UP]:
# 		y -=10
# 	if keys[pygame.K_DOWN]:
# 		y +=10
# 	if x == 20:
# 		x1 +=10
# 		y1 +=10
	
# 	pygame.draw.rect(screen, LIGHT_GRAY, (x, y, x1, y1))
# 	print(x, y)
# 	pygame.time.delay(10)
# 	pygame.display.flip()

		
		
			

	

