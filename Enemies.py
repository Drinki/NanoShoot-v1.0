import pygame
from random import randint
from Missile import *

class Enemy:
	def __init__(self, window, identifiant):
		self.window = window
		self.id = identifiant
		self.width, self.height = self.window.get_size()
		self.image = pygame.image.load("Images/Mobs/mob1.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = randint((self.width//6)*2, (self.width//6)*4)
		self.rect.y = -64
		self.life = 100
		self.speedX = randint(4, 7)
		self.speedY = 6
		self.point = 50
		self.missileEnemie = None
		self.idMissile = 0

	def move(self):
		if self.rect.x <= self.width//2:
			self.rect.x -= self.speedX
			self.rect.y += self.speedY
		else:
			self.rect.x += self.speedX
			self.rect.y += self.speedY

	def display(self):
		self.window.blit(self.image, self.rect)

	def isNotOnScreen(self):
		if self.rect.x > self.width+64 or self.rect.y > self.height or self.rect.x < -64 or self.rect.y < -64:
			return True

	def getLife(self):
		return self.life

	def shoot(self, dicoMissilesEnemies, idMissiles):
		# Création d'un nouveau missile
		self.missileEnemie = MissileEnemies(self.window, idMissiles)
		self.missileEnemie.initPosition(self.rect)
		dicoMissilesEnemies[idMissiles] = self.missileEnemie

	def getPosition(self):
		return self.rect

	def getId(self):
		return self.id

class Enemy2(Enemy):
	def __init__(self, window, identifiant, posPlayerX, posPlayerY):
		Enemy.__init__(self, window, identifiant)
		self.image = pygame.image.load("Images/Mobs/mob2.png")
		self.rect = self.image.get_rect()
		self.speed = 4
		self.life = 100
		self.point = 100
		self.posPlayerX = posPlayerX
		self.posPlayerY = posPlayerY
		self.posSpawn = randint(0, 2)

		if self.posSpawn == 0:#spawn vers le haut
			self.rect.x = randint(200, self.width - 200)
			self.rect.y = -64
		elif self.posSpawn == 1:#Spawn à droite
			self.rect.x = self.width + 64
			self.rect.y = randint(100, 400)
		else:#Spawn à gauche
			self.rect.x = -64
			self.rect.y = randint(100, 400)

		self.coefX = self.rect.x -32 - self.posPlayerX -64
		self.coefY = self.rect.y -32 - self.posPlayerY -64

	def move(self):
		self.rect.x += -self.coefX//60
		self.rect.y += -self.coefY//60

class Enemy3(Enemy):
	def __init__(self, window, identifiant):
		Enemy.__init__(self, window, identifiant)
		self.image = pygame.image.load("Images/Mobs/mob3.png")
		self.rect = self.image.get_rect()
		self.speed = 4
		self.speedBoost = 8
		self.life = 100
		self.point = 200
		self.rect.x = randint(self.width//6 * 2, self.width//6 * 4)
		self.posSpawn = 0

		if self.rect.x >= self.width//6 * 3:
			self.posSpawn = 1

	def move(self):
		if self.posSpawn == 1:
			if self.rect.y < self.height//8:
				self.rect.x += self.speed
				self.rect.y += self.speed
			else:
				self.rect.x -= self.speedBoost
				self.rect.y += self.speedBoost
		else:
			if self.rect.y < self.height//8:
				self.rect.x -= self.speed
				self.rect.y += self.speed
			else:
				self.rect.x += self.speedBoost
				self.rect.y += self.speedBoost

class Enemy4(Enemy):
	def __init__(self, window, identifiant):
		Enemy.__init__(self, window, identifiant)
		self.image = pygame.image.load("Images/Mobs/mob4.png")
		self.rect = self.image.get_rect()
		self.speed = 4
		self.life = 300
		self.point = 200
		self.rect.y = randint(100, self.height//3)
		self.posSpawn = randint(0, 1)

		if self.posSpawn == 1:#Spawn à gauche
			self.rect.x = -64
		else:#Spawn à droite
			self.rect.x = self.width + 64

	def move(self):
		if self.posSpawn == 1:
			self.rect.x += self.speed
		else:
			self.rect.x -= self.speed

class Enemy5(Enemy):
	def __init__(self, window, identifiant):
		Enemy.__init__(self, window, identifiant)
		self.image = pygame.image.load("Images/Mobs/mob5.png")
		self.rect = self.image.get_rect()
		self.speed = 5
		self.life = 200
		self.point = 100
		self.rect.x = randint(self.width//6, (self.width//6) * 5)
		self.rect.y = -64

	def move(self):
		self.rect.y += self.speed
