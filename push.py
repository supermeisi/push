import pygame
import math

width = 800
height = 600

def main():
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	running = True

	clock = pygame.time.Clock()

	x = width/2
	y = height/2

	vx = 0
	vy = 0

	radius = 10

	while running:
		clock.tick(30)
		screen.fill((0, 0, 0))

		for event in pygame.event.get():
			if(event.type == pygame.MOUSEBUTTONUP):
				pos = pygame.mouse.get_pos()
				dist = math.sqrt((pos[0] - x)**2 + (pos[1] - y)**2)

				print pos[0]/dist, pos[1]/dist

				vx -= (0.25*(pos[0]-x)/dist)
				vy -= (0.25*(pos[1]-y)/dist)

				if radius > 0.1:
					radius -= 0.1

		x += vx
		y += vy

		#print x, y

		if(x < 0 or x > 800):
			vx = -vx

		if(y < 0 or y > 600):
			vy = -vy

		pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)) ,int(radius), 1)

		pygame.display.flip()


if __name__ == '__main__':
    main()