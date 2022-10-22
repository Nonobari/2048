import pygame
import random as rd
from logic import *

class Display:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((540, 620))
        self.name = '  2048 By Noé'
        pygame.display.set_caption(self.name)
        imageBackground = pygame.image.load("assets/background.png")
        imageCases = pygame.image.load("assets/case.png")
        imageTiles = pygame.image.load("assets/tiles.png")
        image2048 = pygame.image.load("assets/2048Logo.png").convert_alpha()
        pygame.display.set_icon(image2048)

        imageScoreBackground = pygame.image.load("assets/scoreBackground.png")
        self.dictImages = {
                        0 : imageCases.subsurface(pygame.Rect(0,0,100,100)),
                        2 : imageTiles.subsurface(pygame.Rect(0,0,100,100)),
                        4 : imageTiles.subsurface(pygame.Rect(100,0,100,100)),
                        8 : imageTiles.subsurface(pygame.Rect(200,0,100,100)),
                        16 : imageTiles.subsurface(pygame.Rect(300,0,100,100)),
                        32 : imageTiles.subsurface(pygame.Rect(0,100,100,100)),
                        64 : imageTiles.subsurface(pygame.Rect(100,100,100,100)),
                        128 : imageTiles.subsurface(pygame.Rect(200,100,100,100)),
                        256 : imageTiles.subsurface(pygame.Rect(300,100,100,100)),
                        512 : imageTiles.subsurface(pygame.Rect(0,200,100,100)),
                        1024 : imageTiles.subsurface(pygame.Rect(100,200,100,100)),
                        2048 : imageTiles.subsurface(pygame.Rect(200,200,100,100)),
                        4096 : imageTiles.subsurface(pygame.Rect(300,200,100,100))
    }
        self.background = imageBackground.subsurface(pygame.Rect(0,0,500,500))
        self.scoreBackground = imageScoreBackground.subsurface(pygame.Rect(0,0,540,620))
        self.cases = self.dictImages[0]
        self.coordCases = [(40+120*i,100+20+120*j) for i in range(4) for j in range(4)]
        self.tableau = [[0 for i in range(4)] for j in range(4)]
        Display.newTile(self,2)
        self.scoreRect = pygame.Rect(245,50,95,30)
        self.highScoreRect = pygame.Rect(370,50,95,30)
        self.font = pygame.font.Font(None, 30)
        

    def blitAllCases(self):
        for coord in self.coordCases:
            self.screen.blit(self.cases, coord)

    def newTile(self,number = 1):
        x = rd.randint(0,3)
        y = rd.randint(0,3)
        for i in range(number):
            while self.tableau[x][y] != 0:
                x,y = rd.randint(0,3),rd.randint(0,3)
            tile = rd.choices([2,4],[0.7,0.3])[0]
            self.tableau[x][y] = tile
    
    def gameOverScreen(self):
        print("Game Over !")
        



    def update(self):
        self.screen.blit(self.scoreBackground,(0,0))
        self.screen.blit(self.background, (20, 100))
        self.textScore = self.font.render(str(score.score), True, (0,0,0))
        self.textHighScore = self.font.render(str(score.highest_score),True,(0,0,0))
        self.screen.blit(self.textScore,self.scoreRect)
        self.screen.blit(self.textHighScore,self.highScoreRect)
        Display.blitAllCases(self)
        for i,lignes in enumerate(self.tableau):
            for j,elt in enumerate(lignes):
                self.screen.blit(self.dictImages[elt],(40+ 120*j,120 + 120*i))
        pygame.display.flip()


