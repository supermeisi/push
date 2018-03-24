import pygame
import math
import random

class Particle:
	def __init__(self, screen, (x,y), radius, vx, vy):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = (255,0,0)
		self.thickness = 1
		self.screen = screen
		self.vx = vx
		self.vy = vy
		self.player = False

	def display(self):
		if(self.player == True):
			self.colour = (255,255,255)

		if(self.radius > self.thickness):
			pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), int(self.radius), self.thickness)

	def move(self, vx, vy):
		if(self.player == True):
			for event in pygame.event.get():
				if(event.type == pygame.MOUSEBUTTONUP):
					pos = pygame.mouse.get_pos()
					dist = math.sqrt((pos[0] - self.x)**2 + (pos[1] - self.y)**2)

					print pos[0] - self.x, pos[1] - self.y

					self.vx -= (0.25*(pos[0]-self.x)/dist)
					self.vy -= (0.25*(pos[1]-self.y)/dist)

					if self.radius > 0.1:
						self.radius -= 0.1

		self.vx += vx
		self.vy += vy

		if(self.x < 0 or self.x > 800):
			self.vx = -self.vx

		if(self.y < 0 or self.y > 600):
			self.vy = -self.vy

		self.x += self.vx
		self.y += self.vy

	def collision(self, particle):
		dist = math.sqrt((particle.x - self.x)**2 + (particle.y - self.y)**2)

		if(dist < (particle.radius + self.radius)):
			self.vx = particle.vx
			self.vy = particle.vy
			if(particle.radius > self.radius):
				particle.radius += 0.1
				self.radius -= 0.1
			else:
				particle.radius -= 0.1
				self.radius += 0.1

	def comparison(self, particle):
		if(self.radius > particle.radius):
			self.colour = (255, 0, 0)
		if(self.radius < particle.radius):
			self.colour = (0, 255, 0)

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
