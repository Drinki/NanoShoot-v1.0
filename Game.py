import pygame
from pygame.locals import *
from Player import *
from Enemies import *
from Bonus import *
from Boss import *

class Game:
	def __init__(self, window):
		self.isOnMenu = True # Savoir si on est sur le menu
		self.isOnMenuRestart = False
		self.replay = False # Savoir si le joueur rejoue
		self.clock = pygame.time.Clock()
		self.play = False # Savoir si le joueur joue
		self.window = window
		self.width, self.height = window.get_size()
		self.background = {} # Dictionnaire contenant tous les backgrounds
		self.imagesBtn = {} # Dictionnaire contenant tous les boutons (pour le menu)
		self.sons = {} # Dictionnaire contenant tous les sons
		self.imagesAnimation = [] # Tableau contenant toutes les images de l'introduction
		self.y = 0 # Pour scrollBackground
		self.assetsCharged = False # Pour savoir si les assets sont chargés
		self.key = None
		self.dicoMissile = None
		self.dicoMissileEnnemies = {}
		self.dicoEnemies = {}
		self.idEnemies = 0
		self.dicoBoss = {}
		self.idBoss = 0
		self.idMissilesEnemies = 0
		self.fontScore = pygame.font.Font("Fonts/fontScore.ttf", 64)
		self.fontLevel = pygame.font.Font("Fonts/fontScore.ttf", 32)
		self.level = 1
		self.levelUp = 0
		""" BONUS """
		self.dicoBonusShield = {}
		self.dicoBonusSpeed = {}
		self.dicoBonusBoost = {}
		self.idBonusShield = 0
		self.idBonusSpeed = 0
		self.idBonusBoost = 0
		""" BOSS """
		self.dicoBoss = {}
		self.spawn = 0
		"""SONS"""
		self.playSongPlay = True
		self.playSongInfos = True
		self.playSongQuit = True
		self.playSongBack = True
		self.playSongMenu = True
		self.playSongGame = True


	""" GESTION DES MENUS """
	def menu(self):
		""" Variables pour centrer les boutons sur l'écran """
		widthBtnPlay = self.imagesBtn['btnPlay'].get_rect().width
		heightBtnPlay = self.imagesBtn['btnPlay'].get_rect().height
		positionBtnPlayX = self.width/2 - (widthBtnPlay / 2)
		positionBtnPlayY = self.height/2 - (heightBtnPlay / 2)

		""" Création des zones de clics """
		btnPlay = self.imagesBtn['btnPlay'].get_rect()
		btnPlay.x, btnPlay.y = positionBtnPlayX, positionBtnPlayY

		btnInfos = self.imagesBtn['btnInfos'].get_rect()
		btnInfos.x, btnInfos.y = positionBtnPlayX, positionBtnPlayY + 140

		btnQuit = self.imagesBtn['btnQuit'].get_rect()
		btnQuit.x, btnQuit.y = positionBtnPlayX, positionBtnPlayY + 280



		while self.isOnMenu:
			"""Musique du menu"""
			if self.playSongMenu:
				self.sons['sonMenu'].play(loops = -1)
				self.playSongMenu = False
			for event in pygame.event.get():
				# Quitter le jeu
				if event.type == QUIT:
					self.isOnMenu = False
				if event.type == pygame.MOUSEMOTION:
					#Bouton Play
					if btnPlay.collidepoint(event.pos):
						self.imagesBtn['btnPlay'] = pygame.image.load("Images/Buttons/on_play_button.png").convert_alpha()
						if self.playSongPlay:
							self.sons['sonBtn'].play()
							self.playSongPlay = False
					else:
						self.imagesBtn['btnPlay'] = pygame.image.load("Images/Buttons/play_button.png").convert_alpha()
						self.playSongPlay = True

					#Bouton Info
					if btnInfos.collidepoint(event.pos):
						self.imagesBtn['btnInfos'] = pygame.image.load("Images/Buttons/on_infos_button.png").convert_alpha()
						if self.playSongInfos:
							self.sons['sonBtn'].play()
							self.playSongInfos = False
					else:
						self.imagesBtn['btnInfos'] = pygame.image.load("Images/Buttons/infos_button.png").convert_alpha()
						self.playSongInfos = True

					#Bouton Quit
					if btnQuit.collidepoint(event.pos):
						self.imagesBtn['btnQuit'] = pygame.image.load("Images/Buttons/on_quit_button.png").convert_alpha()
						if self.playSongQuit:
							self.sons['sonBtn'].play()
							self.playSongQuit = False
					else:
						self.imagesBtn['btnQuit'] = pygame.image.load("Images/Buttons/quit_button.png").convert_alpha()
						self.playSongQuit = True

				if event.type == pygame.MOUSEBUTTONDOWN:
					""" CLIC SUR BTN PLAY """
					if btnPlay.collidepoint(event.pos):
						self.isOnMenu = False
						self.play = True
						self.sons['sonMenu'].fadeout(2000)

					""" CLIC SUR BTN INFOS """
					if btnInfos.collidepoint(event.pos):
						self.menuInfos()

					""" CLIC SUR BTN QUIT """
					if btnQuit.collidepoint(event.pos):
						self.isOnMenu = False
						self.play = False
			pygame.display.flip()

			""" Affichages des informations """
			self.window.blit(self.background['backgroundMenu'], (0, 0))
			# Btn PLAY
			self.window.blit(self.imagesBtn['btnPlay'], (positionBtnPlayX, positionBtnPlayY))
			# Btn Infos
			self.window.blit(self.imagesBtn['btnInfos'], (positionBtnPlayX, positionBtnPlayY + 140))
			# Btn Quit
			self.window.blit(self.imagesBtn['btnQuit'], (positionBtnPlayX, positionBtnPlayY + 280))

	def menuInfos(self):
		btnBack = self.imagesBtn['btnBack'].get_rect()
		btnBack.x, btnBack.y = 100, 100
		isOnMenuInfos = True
		while isOnMenuInfos:
			for event in pygame.event.get():
				if  event.type == pygame.MOUSEMOTION:
					#Bouton Back
					if btnBack.collidepoint(event.pos):
						self.imagesBtn['btnBack'] = pygame.image.load("Images/Buttons/on_back_button.png").convert_alpha()
						if self.playSongBack:
							self.sons['sonBtn'].play()
							self.playSongBack = False
					else:
						self.imagesBtn['btnBack'] = pygame.image.load("Images/Buttons/back_button.png").convert_alpha()
						self.playSongBack = True

				if event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						if btnBack.collidepoint(event.pos):
							isOnMenuInfos = False
			pygame.display.flip()

			self.window.blit(self.background['backgroundInfos'], (0, 0))
			self.window.blit(self.imagesBtn['btnBack'], (100, 100))

	def menuRestart(self):
		""" Variables pour centrer les boutons sur l'écran """
		widthBtnRestart = self.imagesBtn['btnRestart'].get_rect().width
		heightBtnRestart = self.imagesBtn['btnRestart'].get_rect().height
		positionBtnRestartX = self.width/2 - (widthBtnRestart / 2)
		positionBtnRestartY = self.height/2 - (heightBtnRestart / 2)

		""" Création des zones de clics """
		btnRestart = self.imagesBtn['btnRestart'].get_rect()
		btnRestart.x, btnRestart.y = positionBtnRestartX, positionBtnRestartY

		btnQuit = self.imagesBtn['btnQuit'].get_rect()
		btnQuit.x, btnQuit.y = positionBtnRestartX, positionBtnRestartY + 280

		while self.isOnMenuRestart:
			for event in pygame.event.get():
				# Quitter le jeu
				if event.type == QUIT:
					self.isOnMenu = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.isOnMenu = False
				if event.type == pygame.MOUSEMOTION:
					#Bouton Play
					if btnRestart.collidepoint(event.pos):
						self.imagesBtn['btnRestart'] = pygame.image.load("Images/Buttons/on_restart_button.png").convert_alpha()
						if self.playSongPlay:
							self.sons['sonBtn'].play()
							self.playSongPlay = False
					else:
						self.imagesBtn['btnRestart'] = pygame.image.load("Images/Buttons/restart_button.png").convert_alpha()
						self.playSongPlay = True

					#Bouton Quit
					if btnQuit.collidepoint(event.pos):
						self.imagesBtn['btnQuit'] = pygame.image.load("Images/Buttons/on_quit_button.png").convert_alpha()
						if self.playSongQuit:
							self.sons['sonBtn'].play()
							self.playSongQuit = False
					else:
						self.imagesBtn['btnQuit'] = pygame.image.load("Images/Buttons/quit_button.png").convert_alpha()
						self.playSongQuit = True

				if event.type == pygame.MOUSEBUTTONUP:
					""" CLIC SUR BTN RESTART """
					if btnRestart.collidepoint(event.pos):
						self.isOnMenuRestart = False
						self.play = True

					""" CLIC SUR BTN QUIT """
					if btnQuit.collidepoint(event.pos):
						self.isOnMenuRestart = False
						self.isOnMenu = False
						self.play = False
			pygame.display.flip()

			""" Affichages des informations """
			self.window.blit(self.background['backgroundRestart'], (0, 0))
			# Btn PLAY
			self.window.blit(self.imagesBtn['btnRestart'], (positionBtnRestartX, positionBtnRestartY))
			# Btn Quit
			self.window.blit(self.imagesBtn['btnQuit'], (positionBtnRestartX, positionBtnRestartY + 280))

	def menuPause(self):
		""" Variables pour centrer les boutons sur l'écran """
		widthBtnResume = self.imagesBtn['btnResume'].get_rect().width
		heightBtnResume = self.imagesBtn['btnResume'].get_rect().height
		positionBtnResumeX = self.width/2 - (widthBtnResume / 2)
		positionBtnResumeY = self.height/2 - (heightBtnResume / 2)

		""" Création des zones de clics """
		btnResume = self.imagesBtn['btnResume'].get_rect()
		btnResume.x, btnResume.y = positionBtnResumeX, positionBtnResumeY

		btnQuit = self.imagesBtn['btnQuit'].get_rect()
		btnQuit.x, btnQuit.y = positionBtnResumeX, positionBtnResumeY + 280

		isOnMenuPause = True

		pygame.mixer.pause()

		while isOnMenuPause:
			for event in pygame.event.get():
				# Quitter le jeu
				if event.type == QUIT:
					self.isOnMenu = False
				if event.type == pygame.MOUSEMOTION:
					#Bouton Play
					if btnResume.collidepoint(event.pos):
						self.imagesBtn['btnResume'] = pygame.image.load("Images/Buttons/on_resume_button.png").convert_alpha()
						if self.playSongPlay:
							self.sons['sonBtn'].play()
							self.playSongPlay = False
					else:
						self.imagesBtn['btnResume'] = pygame.image.load("Images/Buttons/resume_button.png").convert_alpha()
						self.playSongPlay = True

					#Bouton Quit
					if btnQuit.collidepoint(event.pos):
						self.imagesBtn['btnQuit'] = pygame.image.load("Images/Buttons/on_quit_button.png").convert_alpha()
						if self.playSongQuit:
							self.sons['sonBtn'].play()
							self.playSongQuit = False
					else:
						self.imagesBtn['btnQuit'] = pygame.image.load("Images/Buttons/quit_button.png").convert_alpha()
						self.playSongQuit = True

				if event.type == pygame.MOUSEBUTTONUP:
					""" CLIC SUR BTN RESUME """
					if btnResume.collidepoint(event.pos):
						isOnMenuPause = False
						self.play = True
						pygame.mixer.unpause()

					""" CLIC SUR BTN QUIT """
					if btnQuit.collidepoint(event.pos):
						isOnMenuPause = False
						self.isOnMenu = False
						self.play = False
			pygame.display.flip()

			""" Affichages des informations """
			self.window.blit(self.background['backgroundPause'], (0, 0))
			# Btn Resume
			self.window.blit(self.imagesBtn['btnResume'], (positionBtnResumeX, positionBtnResumeY))
			# Btn Quit
			self.window.blit(self.imagesBtn['btnQuit'], (positionBtnResumeX, positionBtnResumeY + 280))

	def delAllEntities(self):
		self.dicoBoss.clear()
		self.dicoEnemies.clear()
		self.dicoMissile.clear()
		self.dicoMissileEnnemies.clear()
		self.dicoBonusBoost.clear()
		self.dicoBonusSpeed.clear()
		self.dicoBonusShield.clear()
		self.spawn = 0
		self.level = 1

	""" Vérification de la boucle principale du programme """
	def running(self):
		if self.play or self.isOnMenu:
			return True
		else:
			return False

	def run(self):
		pygame.time.set_timer(pygame.USEREVENT, 150) # Tir joueur
		pygame.time.set_timer(pygame.USEREVENT + 1, 1500) # Tir ennemie
		pygame.time.set_timer(pygame.USEREVENT + 2, 5000) # Durée d'un bonus
		pygame.time.set_timer(pygame.USEREVENT + 3, 3000) # Affichage du level

		""" Gestion des touches """

		""" Création des entités """
		player = Player(self.window)

		""" Musique de fond """
		if self.playSongGame:
			self.sons['sonGame'].play(loops = -1)
			self.playSongGame = False

		""" Boucle de jeu """
		while self.play:
			""" GESTION DU SCROLL DU BACKGROUND """
			rel_y = self.y % self.height

			self.window.blit(self.background['backgroundGame1'], (0, rel_y - self.background['backgroundGame1'].get_rect().height))

			if rel_y < self.height:
				self.window.blit(self.background['backgroundGame2'], (0, rel_y))
			if rel_y == (self.height - 2):
				tampon = self.background['backgroundGame1']
				self.background['backgroundGame1'] = self.background['backgroundGame' + str(randint(1, 4))]
				self.background['backgroundGame2'] = tampon

			self.y += 2


			self.clock.tick(60)
			self.getFPS()

			"""Affichage du score"""
			displayScore = self.fontScore.render(str(player.point), 1, (255, 255, 0))
			self.window.blit(displayScore, (100, 100))

			"""Affichage du level"""
			displayLevel = self.fontLevel.render("Level " + str(self.level), 1, (255, 255, 255))
			self.window.blit(displayLevel, (100, 200))

			self.key = pygame.key.get_pressed()

			if self.key[pygame.K_LEFT]: player.move('g')
			if self.key[pygame.K_RIGHT]: player.move('d')
			if self.key[pygame.K_UP]: player.move('h')
			if self.key[pygame.K_DOWN]: player.move('b')
			if self.key[pygame.K_ESCAPE]:
				self.menuPause()
			if player.getLife() <= 0: self.play = False

			for event in pygame.event.get():
				if event.type == QUIT:
					self.play = False

				if event.type == pygame.USEREVENT:
					if self.key[pygame.K_SPACE]:
						player.shoot()

				if event.type == pygame.USEREVENT + 1:
					self.createMissilesEnemies()
					for i in range(4):
						self.createMissileBoss(i)

				self.bonusSpeed(event, player)
				self.bonusShield(event, player)
				self.bonusBoost(event, player)

				self.playerLife(event, player)

			"""SCENARIO DU JEU"""
			if player.point <= 1800:
				self.spawnEnnemies(1000, player)
			if player.point >= 1800:
				if self.spawn == 0:
					self.createBoss(Boss)
					self.spawn += 1
			if player.point >= 6800:
				if self.levelUp == 0:
					self.level += 1
					player.life += 2
					self.levelUp += 1
				self.spawnEnnemies(800, player)
			if player.point >= 9000:
				if self.spawn == 1:
					self.createBoss(Boss2)
					self.spawn += 1
			if player.point >= 14000:
				if self.levelUp == 1:
					self.level += 1
					player.life += 2
					self.levelUp += 1
				self.spawnEnnemies(600, player)
			if player.point >= 16500:
				if self.spawn == 2:
					self.createBoss(Boss3)
					self.spawn += 1
			if player.point >= 21500:
				if self.levelUp == 2:
					self.level += 1
					player.life += 2
					self.levelUp += 1
				self.spawnEnnemies(400, player)
			if player.point >= 24000:
				if self.spawn == 3:
					self.createBoss(Boss4)
					self.spawn += 1


			""" GESTION DU SPAWN DES BONUS """
			self.createBonusSpeed()
			self.createBonusShield()
			self.createBonusBoost()

			self.displayEnemies()
			self.displayBoss()
			self.displayMissile(player)
			self.displayMissilesEnemies()

			self.displayBonus(self.dicoBonusSpeed)
			self.displayBonus(self.dicoBonusShield)
			self.displayBonus(self.dicoBonusBoost)

			if player.isDead():
				self.play = False
				self.isOnMenuRestart = True
				self.delAllEntities()

			player.display(self.dicoEnemies, self.dicoMissileEnnemies, self.dicoBonusSpeed, self.dicoBonusShield, self.dicoBonusBoost, self.dicoBoss)
			player.displayLife()
			pygame.display.flip()


	"""GESTION DES MISSILES"""
	def createMissilesEnemies(self):
		for key in self.dicoEnemies:
			self.dicoEnemies[key].shoot(self.dicoMissileEnnemies, self.idMissilesEnemies)
			self.idMissilesEnemies += 1

	def displayMissilesEnemies(self):
		temp = []

		for key in self.dicoMissileEnnemies:
			self.dicoMissileEnnemies[key].move()

			if self.dicoMissileEnnemies[key].isNotOnScreen():
				temp.append(key)

			self.dicoMissileEnnemies[key].display()

		self.deleteEntities(self.dicoMissileEnnemies, temp)

	def createMissileBoss(self, idDirection):
		for key in self.dicoBoss:
			self.dicoBoss[key].shoot(self.dicoMissileEnnemies, self.idMissilesEnemies, idDirection)
			self.idMissilesEnemies += 1

	def displayMissile(self, player):
		self.dicoMissile = player.getDicoMissile()
		temp = []
		for key in self.dicoMissile:
			self.dicoMissile[key].move()
			self.dicoMissile[key].touchEnemies(self.dicoEnemies, player)
			self.dicoMissile[key].touchBoss(self.dicoBoss, player)
			self.dicoMissile[key].display()

			if self.dicoMissile[key].isNotOnScreen():
				temp.append(key)

		self.deleteEntities(self.dicoMissile, temp)

	def deleteEntities(self, dico, temporyDico):
		for key in temporyDico:
			del dico[key]

	"""GESTION DES ENNEMIS"""
	def createEnemies(self, nameEnemy, player):
		if nameEnemy == Enemy2:
			self.dicoEnemies[self.idEnemies] = nameEnemy(self.window, self.idEnemies, player.getPosX(), player.getPosY())
			self.idEnemies += 1
		else:
			self.dicoEnemies[self.idEnemies] = nameEnemy(self.window, self.idEnemies)
			self.idEnemies += 1

	def displayEnemies(self):
		temp = []
		for key in self.dicoEnemies:
			self.dicoEnemies[key].move()

			if self.dicoEnemies[key].isNotOnScreen():
				temp.append(self.dicoEnemies[key].getId())
			self.dicoEnemies[key].display()

		self.deleteEntities(self.dicoEnemies, temp)

	def spawnEnnemies(self, spawn, player):
		rand = randint(0,  spawn)
		if rand == 10:
			self.createEnemies(Enemy, player)
		elif rand == 20:
			self.createEnemies(Enemy2, player)
		elif rand == 30:
			self.createEnemies(Enemy3, player)
		elif rand == 40:
			self.createEnemies(Enemy4, player)
		elif rand == 50:
			self.createEnemies(Enemy5, player)

	"""GESTION DES BOSS"""
	def createBoss(self, nameBoss):
		self.dicoBoss[self.idBoss] = nameBoss(self.window, self.idBoss)
		self.idBoss += 1

	def displayBoss(self):
		temp = []
		for key in self.dicoBoss:
			self.dicoBoss[key].move()
			self.dicoBoss[key].display()

		self.deleteEntities(self.dicoEnemies, temp)

	"""GESTION DES ASSETS"""
	def loadAssets(self):
		""" Ajout de la musique de fond du menu et des effets sonores"""
		self.sons['sonMenu'] = pygame.mixer.Sound("Sounds/menu.wav")
		self.sons['sonGame'] = pygame.mixer.Sound("Sounds/game.wav")
		self.sons['sonBtn'] = pygame.mixer.Sound("Sounds/button.wav")

		""" Ajout du background du menu """
		self.background['backgroundMenu'] = pygame.image.load("Images/Backgrounds/backgroundMenu.png").convert_alpha()
		self.background['backgroundMenu'] = pygame.transform.smoothscale(self.background['backgroundMenu'], (self.width, self.height))

		""" Ajout du background d'informations """
		self.background['backgroundInfos'] = pygame.image.load("Images/Backgrounds/backgroundInfos.png").convert_alpha()
		self.background['backgroundInfos'] = pygame.transform.smoothscale(self.background['backgroundInfos'], (self.width, self.height))

		""" Ajout du background du restart """
		self.background['backgroundRestart'] = pygame.image.load("Images/Backgrounds/backgroundRestart.png").convert_alpha()
		self.background['backgroundRestart'] = pygame.transform.smoothscale(self.background['backgroundRestart'], (self.width, self.height))

		""" Ajout du background pause """
		self.background['backgroundPause'] = pygame.image.load("Images/Backgrounds/backgroundPause.png").convert_alpha()
		self.background['backgroundPause'] = pygame.transform.smoothscale(self.background['backgroundPause'], (self.width, self.height))

		""" Ajout des backgrounds du jeu """
		# [TODO] A mettre sous forme de boucle

		for i in range(1, 5):
			self.background['backgroundGame' + str(i)] = pygame.image.load("Images/Backgrounds/bg" + str(i) + ".png").convert_alpha()
			self.background['backgroundGame' + str(i)] = pygame.transform.smoothscale(self.background['backgroundGame' + str(i)], (self.width, self.height))

		""" Ajout des boutons """
		self.imagesBtn['btnPlay'] = pygame.image.load("Images/Buttons/play_button.png").convert_alpha()
		self.imagesBtn['btnInfos'] = pygame.image.load("Images/Buttons/infos_button.png").convert_alpha()
		self.imagesBtn['btnQuit'] = pygame.image.load("Images/Buttons/quit_button.png").convert_alpha()
		self.imagesBtn['btnBack'] = pygame.image.load("Images/Buttons/back_button.png").convert_alpha()
		self.imagesBtn['btnRestart'] = pygame.image.load("Images/Buttons/restart_button.png").convert_alpha()
		self.imagesBtn['btnResume'] = pygame.image.load("Images/Buttons/resume_button.png").convert_alpha()

		""" Fin du chargement des fichiers """
		self.assetsCharged = True

	def getFPS(self):
		#print(self.clock.get_fps())
		pass

	def loadAnimation(self):
		for i in range(0, 100):
			if i < 10:
				temp = pygame.image.load("Images/Intro/Slime_0000" + str(i) + ".png")
			else:
				temp = pygame.image.load("Images/Intro/Slime_000" + str(i) + ".png")

			temp = pygame.transform.smoothscale(temp, (self.width, self.height))
			self.imagesAnimation.append(temp)

	def playAnimation(self):
		for i in range(0, len(self.imagesAnimation)):
			self.clock.tick(60)
			self.window.blit(self.imagesAnimation[i], (0, 0))
			pygame.display.flip()

	def displayLoading(self):
		loadingImage = pygame.image.load("Images/loading.png").convert_alpha()
		loadingImage = pygame.transform.smoothscale(loadingImage, (self.width, self.height))
		self.window.blit(loadingImage, (0, 0))
		pygame.display.flip()

	""" GESTION DES BONUS """

	def createBonusSpeed(self):
		for key in self.dicoEnemies:
			if (randint(0, 3000) == 0):
				self.dicoBonusSpeed[self.idBonusSpeed] = Bonus(self.window, self.idBonusSpeed, self.dicoEnemies[key].getPosition())
				self.idBonusSpeed += 1

	def createBonusShield(self):
		for key in self.dicoEnemies:
			if (randint(0, 3000) == 0):
				self.dicoBonusShield[self.idBonusShield] = Bonus_shield(self.window, self.idBonusShield, self.dicoEnemies[key].getPosition())
				self.idBonusShield += 1

	def createBonusBoost(self):
		for key in self.dicoEnemies:
			if (randint(0, 3000) == 0):
				self.dicoBonusBoost[self.idBonusBoost] = Bonus_boost(self.window, self.idBonusBoost, self.dicoEnemies[key].getPosition())
				self.idBonusBoost += 1

	def displayBonus(self, dico):
		temp = []
		for key in dico:
			dico[key].move()
			if dico[key].isNotOnScreen():
				temp.append(dico[key].get_id())

			dico[key].display()
		self.deleteEntities(dico, temp)

	def bonusSpeed(self, event, player):
		# Signifie qu'il vient d'avoir un bonus
		if player.getBonusSpeed == False:
			pygame.time.set_timer(pygame.USEREVENT, 75)
			if event.type == pygame.USEREVENT + 2:
				player.speed = 15
				pygame.time.set_timer(pygame.USEREVENT, 150)
				player.getBonusSpeed = True

	def bonusShield(self, event, player):
		if player.getBonusShield == False:
			# Changement de l'image
			player.image = pygame.image.load("Images/playerShield.png").convert_alpha()
			if event.type == pygame.USEREVENT + 2:
				player.canTouch = True
				player.image = pygame.image.load("Images/player.png").convert_alpha()
				player.getBonusShield = True

	def bonusBoost(self, event, player):
		if player.getBonusBoost == False:
			for key in self.dicoMissile:
				self.dicoMissile[key].image = pygame.image.load("Images/Missiles/missilePlayerBoost.png").convert_alpha()
				self.dicoMissile[key].damage = 600

			if event.type == pygame.USEREVENT + 2:
				player.getBonusBoost = True

	""" GESTION DE LA VIE DU JOUEUR """
	def playerLife(self, event, player):
		if player.canTouch == False and player.getBonusShield == True:
			player.image = pygame.image.load("Images/playerOpac.png").convert_alpha()
			if event.type == pygame.USEREVENT + 2:
				player.image = pygame.image.load("Images/player.png").convert_alpha()
				player.canTouch = True
