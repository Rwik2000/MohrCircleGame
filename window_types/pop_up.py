import pygame
# import MohrCircle_new
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
from utilities.mohr_screen import *
def incompatible_input_window(screen):
    backButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                generalwindow_check.makeCurrent()
                general2D_input_window_check.endCurrent()
            
        if event.type == pygame.MOUSEMOTION:
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

