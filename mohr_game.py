import pygame
# import MohrCircle_new
from MohrCircle_new import execute
import window_types.mohr_quiz as mohr_quiz
import window_types.mohr_general as mohr_general
import window_types.pop_up as pop_up
import window_types.mohr_initial as mohr_initial
from mohr_window_list import windows
import time
import random
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
from utilities.mohr_screen import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mohr's Circle")

startwindow_check.makeCurrent()

def det_curr_prev(curr_win,prev_win,window_name):
    if curr_win!=window_name:
        prev_win = curr_win
        curr_win = window_name
        print("prev win : "+ prev_win)
        print("curr win : "+ curr_win)
    return curr_win, prev_win

def window_check(curr_win, prev_win, window, window_attr, screen):
    if window_attr[1].checkUpdate():
        curr_win, prev_win = det_curr_prev(curr_win,prev_win,window_attr[0])
        window(screen)
    return screen, curr_win, prev_win

# Game Loop
running =True
count = 0
curr_win = 'startwindow'
prev_win = 'startwindow'
while running:
    screen.fill((255,255,255))
    for win in windows.keys():
        screen, curr_win, prev_win=window_check(curr_win, prev_win, win, windows[win], screen)
    

    pygame.display.update()