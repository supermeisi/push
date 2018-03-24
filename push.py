import pygame
import math
import random
from particle import Particle

def main():
	width = 800
	height = 600

	pygame.init()
	screen = pygame.display.set_mode((width, height))
	running = True

	clock = pygame.time.Clock()

	x = width/2
	y = height/2

	vx = 0
	vy = 0

	radius = 20

	particles = []

	player = Particle(screen, (int(x), int(y)), int(radius), 0, 0)

	player.player = True

	particles.append(player)

	lost = False

	#Creating initial particles randomly
	for i in range(20):
		randx = random.random()*800
		randy = random.random()*640

		randvx = -2+random.random()*4
		randvy = -2+random.random()*4

		randrad = 30*random.random()+1

		print randvx, randvy

		particle = Particle(screen, (randx, randy), int(randrad), int(randvx), int(randvy))

		#Adding particles to particle list
		particles.append(particle)

	#Define text output
	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 30)

	#Starting main loop
	while running:
		clock.tick(30)
		screen.fill((0, 0, 0))

		index = []

		for i in range(len(particles)):
			particles[i].display()
			particles[i].move(0, 0)

			particles[i].comparison(player)

			for j in range(len(particles)):
				particles[i].collision(particles[j])

			if(particles[i].radius < particles[i].thickness):
				index.append(i)
				if(particles[i].player == True):
					lost = True
					print "You lost the game"

		for i in range(len(index)):
			particles.pop(index[i])

		player.display()
		player.move(0, 0)

		if(lost == True):
			textsurface = myfont.render("You lost the game", False, (255, 55, 0))
			screen.blit(textsurface,(width/2,height/2))

		pygame.display.flip()


if __name__ == '__main__':
    main()
