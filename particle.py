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

	def move(self, world_width, world_height, vx, vy):
		self.vx += vx
		self.vy += vy

		if(self.x < 0 or self.x > world_width):
			self.vx = -self.vx

		if(self.y < 0 or self.y > world_height):
			self.vy = -self.vy

		self.x += self.vx
		self.y += self.vy

	def collision(self, particle):
		dist = math.sqrt((particle.x - self.x)**2 + (particle.y - self.y)**2)

		if(dist < (particle.radius + self.radius)):
			#Calculate the center-of-mass speed of both particles
			self.vx = (self.radius*self.vx + particle.radius*particle.vx)/(self.radius + particle.radius)
			particle.vx = self.vx
			self.vy = (self.radius*self.vy + particle.radius*particle.vy)/(self.radius + particle.radius)
			particle.vy = self.vy

			#Check which particle is bigger
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

	def shift(self, dx, dy):
		self.x += dx
		self.y += dy

	def shrink(self, dr):
		self.radius += dr