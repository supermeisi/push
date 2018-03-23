import pygame
import math

width = 800
height = 600

class Particle:
	def __init__(self, screen, (x,y), radius, vx, vy):
		self.x = x
		self.y = y
		self.radius = radius
		self.colour = (255,255,255)
		self.thickness = 1
		self.screen = screen
		self.vx = vx
		self.vy = vy

	def display(self):
		pygame.draw.circle(self.screen, self.colour, (int(self.x), int(self.y)), self.radius, self.thickness)

	def move(self, vx, vy):
		self.vx = vx
		self.vy = vy

		self.x += self.vx
		self.y += self.vy

		if(self.x < 0 or self.x > 800):
			self.vx = -self.vx

		if(self.y < 0 or self.y > 600):
			self.vy = -self.vy

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

	particles = []

	particle = Particle(screen, (50, 50), 15, 0, 0)

	particles.append(particle)

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

		if(x < 0 or x > 800):
			vx = -vx

		if(y < 0 or y > 600):
			vy = -vy

		for i in range(len(particles)):
			particles[i].display()
			particles[i].move(2, 1.5)

		pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)) ,int(radius), 1)

		pygame.display.flip()


if __name__ == '__main__':
    main()
