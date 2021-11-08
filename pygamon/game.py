import pygame
import pytmx
import pyscroll


class Game:

    def __init__(self):
        #créer la fenêtre de jeu
        self.screen = pygame.display.set_mode((800, 600))      #on définit la taille de la fenêtre
        pygame.display.set_caption("Pygamon - Adventure")         #changement du titre de la fenetre


        #charger la carte
        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        #dessin du grpe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        #boucle du jeu
        running = True

        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()