import pygame
from random import randint
from Player import *

class Missile:
	def __init__(self, window, identifiant):
		self.window = window
		self.width, self.height = self.window.get_size()
		self.damage = 100
		self.id = identifiant
		self.image = pygame.image.load("Images/Missiles/missilePlayer.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.speed = 20
		self.delete = False

	# Mouvement du missile
	def move(self):
		self.rect.y -= self.speed

	def initPosition(self, playerPostion):
		if randint(0, 1) == 0:
			""" Pour coller l'image du missile au canon de gauche """
			self.rect.x = playerPostion.x + 27
			self.rect.y = playerPostion.y
		else:
			""" Pour coller l'image du missile au canon de droite """
			self.rect.x = playerPostion.x + 62
			self.rect.y = playerPostion.y


	def display(self):
		self.window.blit(self.image, self.rect)

	""" Renvoie l'identifiant du missile """
	def getId(self):
		return self.id

	""" Renvoie si le missile est supprimé """
	def isDelete(self):
		return self.delete

	""" Savoir si le missile quitte l'écran """
	def isNotOnScreen(self):
		if self.rect.y <= - 16:
			return True

	def touchEnemies(self, dicoEnemies, player):
		arrayTouchedEnemies = []

		# Collision missilePlayer - ennemis
		for key in dicoEnemies:
			if self.rect.colliderect(dicoEnemies[key]):
				dicoEnemies[key].life -= self.damage
				self.rect.y = -16
				self.delete = True
				if dicoEnemies[key].getLife() <= 0:
					arrayTouchedEnemies.append(key)
					player.addPoint(dicoEnemies[key].point)

		for i in range(len(arrayTouchedEnemies)):
			del dicoEnemies[arrayTouchedEnemies[i]]

	def touchBoss(self, dicoBoss, player):
		arrayTouchedBoss = []

		for key in dicoBoss:
			if self.rect.colliderect(dicoBoss[key]):
				dicoBoss[key].life -= self.damage
				self.rect.y = -16
				self.delete = True
				if dicoBoss[key].getLife() <= 0:
					arrayTouchedBoss.append(key)
					player.addPoint(dicoBoss[key].point)

		for i in range(len(arrayTouchedBoss)):
			del dicoBoss[arrayTouchedBoss[i]]

class MissileEnemies(Missile):
	def __init__(self, window, identifiant):
		Missile.__init__(self, window, identifiant)
		self.speed = 10
		self.image = pygame.image.load("Images/Missiles/missileEnemies.png").convert_alpha()

	def move(self):
		self.rect.y += self.speed

	def isNotOnScreen(self):
		if self.rect.y >= self.height + 16 :
			return True

	def initPosition(self, enemiesPosition):
		self.rect.x = enemiesPosition.x + 58
		self.rect.y = enemiesPosition.y + 130

class MissileBoss(Missile):
	def __init__(self, window, identifiant, idDirection):
		Missile.__init__(self, window, identifiant)
		self.speed = 6
		self.image = pygame.image.load("Images/Missiles/missileBoss.png")
		self.idDirection = idDirection

	def move(self):
		if self.idDirection == 1 or self.idDirection == 2:
			self.rect.x -= self.speed
			self.rect.y += self.speed
		else:
			self.rect.x += self.speed
			self.rect.y += self.speed

	def isNotOnScreen(self):
		if self.rect.y >= self.height + 16 :
			return True

	def initPosition(self, posBoss):
		if self.idDirection == 1:
			self.rect.x = posBoss.x + 64
			self.rect.y = posBoss.y + 512
		elif self.idDirection == 2:
			self.rect.x = posBoss.x + 128
			self.rect.y = posBoss.y + 512
		elif self.idDirection == 3:
			self.rect.x = posBoss.x + 192
			self.rect.y = posBoss.y + 512
		else:
			self.rect.x = posBoss.x + 256
			self.rect.y = posBoss.y + 512
