import pygame
import MohrCircle
from MohrCircle import mohrCircle_execute
import window_types.mohr_quiz as mohr_quiz
import window_types.mohr_general as mohr_general
import time
import random
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
from utilities.mohr_screen import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mohr's Circle")

iitgn_logo = pygame.image.load("Images/iitgn.png")
iitgn_logo = pygame.transform.scale(iitgn_logo, (250, 250))

def startwindow(screen):
    Big_font = game_font(80)
    Small_font = game_font(20)
    text = Big_font.render("Mohr's Circle", 1, (0,0,0))
    screen.blit(text, (70, 250))
    screen.blit(iitgn_logo, (280,0))
    text = Small_font.render ("An interactive app to understand and visualise the concepts of Mohr's Circle in 2-Dimeansion and 3-Dimension",1, (0,0,0))
    screen.blit(text, (60, 400))
    text = Small_font.render ("Rwik Rana| Shreyas Sonawane| Manish Alriya| Yash Meshram ",1, (0,0,0))
    screen.blit(text, (60, 550))
    enterButton.draw(screen, (0,0,0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if enterButton.isOver(pos):
                enterWindow_check.makeCurrent()
                startwindow_check.endCurrent()
                print("User entered the Application")
        if event.type == pygame.MOUSEMOTION:
            if enterButton.isOver(pos):
                enterButton.color = (255, 0, 0)
            else:
                enterButton.color = (180, 0, 0)

def enterwindow(screen):
    Small_font = game_font(20)
    text = Small_font.render ("Select Mode",1, (0,0,0))
    screen.blit(text, (360, 100))

    generalButton.draw(screen, (0,0,0))
    tutorialButton.draw(screen, (0,0,0))
    quizButton.draw(screen, (0,0,0))
    backButton.draw(screen, (0,0,0))


    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if generalButton.isOver(pos):
                generalwindow_check.makeCurrent()
                enterWindow_check.endCurrent()
                print("Entering in General Mode")
            if quizButton.isOver(pos):
                quizwindow_check.makeCurrent()
                enterWindow_check.endCurrent()
                print("Entering in Quiz Mode")
            if backButton.isOver(pos):
                startwindow_check.makeCurrent()
                enterWindow_check.endCurrent()
        if event.type == pygame.MOUSEMOTION:
            if generalButton.isOver(pos):
                generalButton.color = (255, 0, 0)
            else:
                generalButton.color = (180, 0, 0) 
            if tutorialButton.isOver(pos):
                tutorialButton.color = (255, 0, 0)
            else:
                tutorialButton.color = (180, 0, 0) 
            if quizButton.isOver(pos):
                quizButton.color = (255, 0, 0)
            else:
                quizButton.color = (180, 0, 0) 
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

startwindow_check.makeCurrent()


# Game Loop
running =True
while running:
    screen.fill((255,255,255))

    if startwindow_check.checkUpdate():
        startwindow(screen)
    if enterWindow_check.checkUpdate():
        enterwindow(screen)


    if generalwindow_check.checkUpdate():
        mohr_general.generalwindow(screen)
    if general2D_input_window_check.checkUpdate():
        mohr_general.general2D_input_window(screen)
    if general3D_input_window_check.checkUpdate():
        mohr_general.general3D_input_window(screen)

    if quizwindow_check.checkUpdate():
        mohr_quiz.quizwindow(screen)
    if quizwindow_2d_check.checkUpdate():
        mohr_quiz.quizwindow_2d(screen)
    if quizwindow_3d_check.checkUpdate():
        mohr_quiz.quizwindow_3d(screen)
    if quizwindow_concept_check.checkUpdate():
        mohr_quiz.quizwindow_concept(screen)
    if quiz_end_window_check.checkUpdate():
        mohr_quiz.quiz_end_window(screen)

    pygame.display.update()