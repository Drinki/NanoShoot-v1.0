import pygame
from Enemies import *

class Bonus:
    def __init__(self, window, identifiant, pos_enemy):
        self.screen = window
        self.width, self.height = window.get_size()
        self.image = pygame.image.load("Images/Bonus/bonusSpeed.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.id = identifiant
        self.speed = 7
        self.pos_enemy = pos_enemy
        self.rect.x = self.pos_enemy.x + 16
        self.rect.y = self.pos_enemy.y + 32

    #Mouvement du missile
    def move(self):
        self.rect.y += self.speed

    #Renvoie d'id du bonus
    def get_id(self):
        return self.id

    #Detecte si le bonus est dans l'écran
    def isNotOnScreen(self):
        if self.rect.x > self.width+64 or self.rect.y > self.height or self.rect.x < -64 or self.rect.y < -64:
            return True

    #Affiche le bonus à l'écran
    def display(self):
        self.screen.blit(self.image, self.rect)

class Bonus_shield(Bonus):
    def __init__(self, window, identifiant, pos_enemy):
        Bonus.__init__(self, window, identifiant, pos_enemy)
        self.image = pygame.image.load("Images/Bonus/bonusShield.png").convert_alpha()

class Bonus_boost(Bonus):
    def __init__(self, window, identifiant, pos_enemy):
        Bonus.__init__(self, window, identifiant, pos_enemy)
        self.image = pygame.image.load("Images/Bonus/bonusBoost.png").convert_alpha()
