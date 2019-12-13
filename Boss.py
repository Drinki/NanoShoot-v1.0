import pygame
from Missile import *
from random import randint

class Boss:
    def __init__(self, window, identifiant):
        self.window = window
        self.width, self.height = window.get_size()
        self.image = pygame.image.load("Images/Boss/bossPoumon.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = -512
        self.rect.x = self.width//2 -256
        self.id = identifiant
        self.speed = 3
        self.life = 4000
        self.dirMove = 0
        self.missileEnemie = None
        self.point = 5000

    def move(self):
        if self.rect.y <= 100:
            self.rect.y += self.speed

        elif self.dirMove == 0:
            if self.rect.x != 100 or self.rect.x <= 100:
                self.rect.x -= self.speed
            if self.rect.x <= 100:
                self.dirMove = 1
        elif self.dirMove == 1:
            if self.rect.x != self.width - 512 or self.rect.x <= self.width - 512:
                self.rect.x += self.speed
            if self.rect.x >= self.width - 512:
                self.dirMove = 0

    def getLife(self):
        return self.life

    def shoot(self, dicoMissileEnnemies, idMissilesEnemies, idDirection):
        self.missileEnemie = MissileBoss(self.window, self.id, idDirection)
        self.missileEnemie.initPosition(self.rect)
        dicoMissileEnnemies[idMissilesEnemies] = self.missileEnemie

    def display(self):
        self.window.blit(self.image, self.rect)

class Boss2(Boss):
    def __init__(self, window, identifiant):
        Boss.__init__(self, window, identifiant)
        self.image = pygame.image.load("Images/Boss/bossFoie.png")
        self.rect = self.image.get_rect()
        self.rect.y = -512
        self.rect.x = self.width//2 - 256
        self.speed = 4
        self.life = 6000
        self.point = 5000

class Boss3(Boss):
    def __init__(self, window, identifiant):
        Boss.__init__(self, window, identifiant)
        self.image = pygame.image.load("Images/Boss/bossCoeur.png")
        self.rect = self.image.get_rect()
        self.rect.y = -512
        self.rect.x = self.width//2 - 256
        self.speed = 4
        self.life = 8000
        self.point = 5000

class Boss4(Boss):
    def __init__(self, window, identifiant):
        Boss.__init__(self, window, identifiant)
        self.image = pygame.image.load("Images/Boss/bossCerveau.png")
        self.rect = self.image.get_rect()
        self.rect.y = -512
        self.rect.x = self.width//2 - 256
        self.speed = 4
        self.life = 10000
        self.point = 5000
