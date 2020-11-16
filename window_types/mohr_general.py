
import pygame
import numpy as np
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
import random
from utilities.mohr_screen import *

def generalwindow(screen):
    Small_font = game_font(20)
    text = Small_font.render("General Mode",1, (0,0,0))
    screen.blit(text, (360, 100))

    twodButton.draw(screen, (0,0,0))
    threedButton.draw(screen, (0,0,0))
    backButton.draw(screen, (0,0,0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if twodButton.isOver(pos):
                general2D_input_window_check.makeCurrent()
                generalwindow_check.endCurrent()
                # global s, a
                # a = 1
                # A.append(a)
                # s = s + 1
                print("Entering in 2-D Mode")
            if threedButton.isOver(pos):
            #     a = 2
            #     A.append(a)
            #     s = s + 1
                general3D_input_window_check.makeCurrent()
                generalwindow_check.endCurrent()
                print("Entering in 3-D Mode")
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                generalwindow_check.endCurrent()
                # s = s - 1
                # A.pop()

        if event.type == pygame.MOUSEMOTION:
            if twodButton.isOver(pos):
                twodButton.color = (255, 0, 0)
            else:
                twodButton.color = (180, 0, 0)
            if threedButton.isOver(pos):
                threedButton.color = (255, 0, 0)
            else:
                threedButton.color = (180, 0, 0)
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

def general2D_input_window(screen): 
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_gen:"σxx", sigma_yy_gen:"σyy", sigma_xy_gen:"σxy"}
    Small_font = game_font(20)
    head_text = Small_font.render("General 2- D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 80, box.y))

    screen.blit(head_text, (360, 100))  
    backButton.draw(screen, (0,0,0))
    enterButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                generalwindow_check.makeCurrent()
                general2D_input_window_check.endCurrent()
                # global s
                # s = s - 1
                # A.pop()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                for box in input_boxes.keys():
                    mohrCircle_input.append(float(box.text))

                if len(mohrCircle_input) == 3:
                    for i in range(3):
                        mohrCircle_input.append(0)
                    mohrCircle_execute(2, mohrCircle_input)
                    time.sleep(10)
                    
                else:
                    print("Insufficient data")
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = not box.active
                else:
                    box.active = False
        if event.type == pygame.KEYDOWN:
            
            for box in input_boxes.keys():
                if box.active:
                    if event.key == pygame.K_RETURN:
                        print(box.text)
                        box.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        box.text = box.text[:-1]
                    else:
                        try:
                            _=float(event.unicode)
                            box.text += event.unicode    
                        except:
                            if event.unicode == ".":
                                temp_text = box.text
                                temp_text +=event.unicode
                                try:
                                    float(temp_text)
                                    box.text +=event.unicode   
                                except:
                                    pass   

        if event.type == pygame.MOUSEMOTION:
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)


    for box in input_boxes.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)


def general3D_input_window(screen): 
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_gen:"σxx", sigma_yy_gen:"σyy", sigma_xy_gen:"σxy", sigma_zz_gen:"σzz", sigma_yz_gen:"σyz", sigma_zx_gen:"σzx"}
    Small_font = game_font(20)
    head_text = Small_font.render("General 3-D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 80, box.y))

    screen.blit(head_text, (360, 100))  
    backButton.draw(screen, (0,0,0))
    enterButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                generalwindow_check.makeCurrent()
                general3D_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                for box in input_boxes.keys():
                    mohrCircle_input.append(float(box.text))

                if len(mohrCircle_input) == 6:
                    mohrCircle_execute(3, mohrCircle_input)
                    time.sleep(10)
                    
                else:
                    print("Insufficient data")
                    
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = not box.active
                else:
                    box.active = False
        if event.type == pygame.KEYDOWN:
            
            for box in input_boxes.keys():
                if box.active:
                    if event.key == pygame.K_RETURN:
                        print(box.text)
                        box.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        box.text = box.text[:-1]
                    else:
                        try:
                            _=float(event.unicode)
                            box.text += event.unicode    
                        except:
                            if event.unicode == ".":
                                temp_text = box.text
                                temp_text +=event.unicode
                                try:
                                    float(temp_text)
                                    box.text +=event.unicode   
                                except:
                                    pass   

        if event.type == pygame.MOUSEMOTION:
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)


    for box in input_boxes.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)