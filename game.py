import pygame
from display import Display
from logic import *

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display = Display()
        self.currentTab = self.display.tableau
        self.tabList = [self.currentTab]

    def run(self):
        continuer = True
        while continuer:
            self.display.update()
            event = pygame.event.wait()
            continuer = Game.game_overCheck(self)

            if event.type == pygame.KEYDOWN:
                #Mémoire du dernier coup pour retour arrière
                if not(self.currentTab == self.display.tableau):
                    self.currentTab = self.display.tableau 

                    if len(self.tabList)>2:
                        self.tabList.pop(-3) 
                    self.tabList.append(self.currentTab)

                if event.key == pygame.K_ESCAPE:
                    self.display.tableau = self.tabList[-2]
                    self.display.update()

                if event.key == pygame.K_LEFT:
                    self.display.tableau,temp = move_left(self.display.tableau)
                    if not any(0 in row for row in self.display.tableau):
                        pass
                    else:
                        if not(self.currentTab == self.display.tableau):
                            self.display.newTile()

                if event.key == pygame.K_RIGHT:
                    self.display.tableau,temp = move_right(self.display.tableau)
                    if not any(0 in row for row in self.display.tableau):
                        pass
                    else:
                        if not(self.currentTab == self.display.tableau):
                            self.display.newTile()


                if event.key == pygame.K_UP:
                    self.display.tableau,temp = move_up(self.display.tableau)
                    if not any(0 in row for row in self.display.tableau):
                        pass
                    else:
                        if not(self.currentTab == self.display.tableau):
                            self.display.newTile()


                if event.key == pygame.K_DOWN:
                    self.display.tableau,temp = move_down(self.display.tableau)
                    if not any(0 in row for row in self.display.tableau):
                        pass
                    else:
                        if not(self.currentTab == self.display.tableau):
                            self.display.newTile()

            if event.type == pygame.QUIT:
                continuer = False
                pygame.quit()


    def game_overCheck(self):
            if any(2048 in row for row in self.display.tableau):
                print("Vous avez gagné !")    
                return True   
            elif not any(0 in row for row in self.display.tableau) and not Exists_horizontalMoves(self.display.tableau) and not Exists_verticalMoves(self.display.tableau):
                self.display.gameOverScreen()
                score.save()
                score.sayHighestScore(score.score)

                return False
            else: return True