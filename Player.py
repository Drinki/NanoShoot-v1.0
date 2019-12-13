import pygame
from Missile import *

class Player:
	def __init__(self, window):
		self.window = window
		self.width, self.height = window.get_size()
		self.image = pygame.image.load("Images/player.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = (window.get_width()//2) - self.image.get_width()//2
		self.rect.y = window.get_height() - (self.image.get_height() * 1.5)
		self.speed = 15
		self.dicoMissile = {}
		self.idMissile = 0
		self.getBonusSpeed = True
		self.getBonusShield = True
		self.getBonusBoost = True
		self.canTouch = True
		self.point = 0

		"""LA VIE"""
		self.life = 6
		self.imageLife = pygame.image.load("Images/Lifes/life_6.png").convert_alpha()
		self.imageLifeRect = self.imageLife.get_rect()
		self.imageLifeRect.x = self.width//6 * 5
		self.imageLifeRect.y = self.height//20


	def move(self, direction):
		""" Gestion du déplacement du joueur """
		if direction == "d":
			self.rect.x += self.speed
		elif direction == "g":
			self.rect.x -= self.speed
		elif direction == "h":
			self.rect.y -= self.speed
		else:
			self.rect.y += self.speed

		""" Gestion limite de l'écran"""
		if self.rect.x >= self.width - 128:
			self.rect.x -= self.speed
		elif self.rect.x <= 0:
			self.rect.x += self.speed
		elif self.rect.y >= self.height - 128:
			self.rect.y -= self.speed
		elif self.rect.y <= 0:
			self.rect.y += self.speed

	def isTouched(self, dicoEnemies, dicoMissilesEnemies, dicoBonusSpeed, dicoBonusShield, dicoBonusBoost, dicoBoss):
		temp = []
		temp.append(dicoEnemies) #0
		temp.append(dicoMissilesEnemies) #1
		temp.append(dicoBonusSpeed) #2
		temp.append(dicoBonusShield) #3
		temp.append(dicoBonusBoost) #4
		temp.append(dicoBoss) #5

		for key in temp[0]:
			if self.canTouch:
				if self.rect.colliderect(temp[0][key]):
					self.looseLife()

		for key in temp[1]:
			if self.canTouch:
				if self.rect.colliderect(temp[1][key]):
					self.looseLife()
					temp[1][key].rect.y = self.height + 16

		for key in temp[2]:
			if self.getBonusSpeed:
				if self.rect.colliderect(temp[2][key]):
					self.bonusSpeed()
					temp[2][key].rect.y = -50 # Pour supprimer le bonus


		for key in temp[3]:
			if self.getBonusShield:
				if self.rect.colliderect(temp[3][key]):
					self.bonusShield()
					temp[3][key].rect.y = -50 # Pour supprimer le bonus


		for key in temp[4]:
			if self.getBonusBoost:
				if self.rect.colliderect(temp[4][key]):
					self.bonusBoost()
					temp[4][key].rect.y = -50 # Pour supprimer le bonus

		for key in temp[5]:
			if self.canTouch:
				if self.rect.colliderect(temp[5][key]):
					self.looseLife()

	def display(self, dicoEnemies, dicoMissilesEnemies, dicoBonusSpeed, dicoBonusShield, dicoBonusBoost, dicoBoss):
		self.isTouched(dicoEnemies, dicoMissilesEnemies, dicoBonusSpeed, dicoBonusShield, dicoBonusBoost, dicoBoss)
		self.window.blit(self.image, self.rect)
		self.window.blit(self.imageLife, self.imageLifeRect)

	def addPoint(self, enemyPoint):
		self.point += enemyPoint

	def shoot(self):
		# Création d'un nouveau missile
		newMissile = Missile(self.window, self.idMissile)
		newMissile.initPosition(self.rect)
		self.dicoMissile[self.idMissile] = newMissile
		self.idMissile += 1

	def getDicoMissile(self):
		# Renvoie le dictionnaire des missiles dans le jeu
		return self.dicoMissile

	""" GESTION DES BONUS """
	def bonusSpeed(self):
		self.speed = 30
		self.getBonusSpeed = False

	def bonusShield(self):
		self.canTouch = False
		self.getBonusShield = False

	def bonusBoost(self):
		self.getBonusBoost = False

	"""GESTION DE LA VIE"""
	def looseLife(self):
		self.life -= 1
		self.canTouch = False

	def getLife(self):
		return self.life

	def isDead(self):
		if self.life <= 0:
			return True

	def displayLife(self):
		if self.life == 5:
			self.imageLife = pygame.image.load("Images/Lifes/life_5.png").convert_alpha()
		elif self.life == 4:
			self.imageLife = pygame.image.load("Images/Lifes/life_4.png").convert_alpha()
		elif self.life == 3:
			self.imageLife = pygame.image.load("Images/Lifes/life_3.png").convert_alpha()
		elif self.life == 2:
			self.imageLife = pygame.image.load("Images/Lifes/life_2.png").convert_alpha()
		elif self.life == 1:
			self.imageLife = pygame.image.load("Images/Lifes/life_1.png").convert_alpha()

	"""GESTION DE LA POSITION DU JOUEUR"""
	def getPosX(self):
		return self.rect.x

	def getPosY(self):
		return self.rect.y
