import pygame
import math

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