# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:30:08 2019

@author: JessicaSpencer
"""
import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """creates the game, and creates game resources"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """start main loop for game."""
        while True:
            """watch for keyboard and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #makes the most recently drawn screen visible
            pygame.display.flip()
    
    
if __name__== '__main__':
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
            