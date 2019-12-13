import pygame
from random import randint
from Game import *

# Initialisation de pygame et création de la fenêtre
pygame.init()
window = pygame.display.set_mode((0,0), FULLSCREEN)

# Création de l'objet game
game = Game(window)

# Chargement des assets graphiques et sonores
game.displayLoading() # Affichage du cdhargement
game.loadAssets() # Chargement des assets, du jeu
game.loadAnimation() # Chargement des images d'animations (intro du jeu)

# Affichage de l'intro du jeu
game.playAnimation()

# Démarage de la boucle du menu
while game.running():
	game.menu()
	game.run()
	game.menuRestart()



# Fermeture de l'application
pygame.quit()
