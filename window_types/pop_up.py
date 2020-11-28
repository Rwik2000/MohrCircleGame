import pygame
import numpy as np
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
import random
from utilities.mohr_screen import *
from MohrCircle_stress_2 import Stress_MohrCircle
from MohrCircle_strain_2 import Strain_MohrCircle
from MohrCircle_strain import strain_execute

stress_strain_win_select = [0,0]
def generalwindow(screen, prev_win, windows):
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
                if(stress_strain_win_select[0] == 1):
                    gen2D_stress_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in stress 2-D Mode")
                else:
                    gen2D_strain_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in strain 2-D Mode")
            if threedButton.isOver(pos):
                if(stress_strain_win_select[0]==1):
                    gen3D_stress_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in 3-D Mode")
                else:
                    gen3D_strain_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in strain 2-D Mode")
            if backButton.isOver(pos):
                stress_strain_window_check.makeCurrent()
                generalwindow_check.endCurrent()

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
def box_text_input(event, input_boxes):
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
                        if event.unicode == "." or event.unicode == "-":
                            temp_text = box.text
                            temp_text +=event.unicode
                            try:
                                float(temp_text)
                                box.text +=event.unicode   
                            except:
                                if len(box.text) == 0:
                                    if event.unicode == "-" or event.unicode=='.':
                                        box.text +=event.unicode 

def stress_strain_window(screen, prev_win, windows):
    global stress_strain_win_select
    stress_strain_win_select = [0,0]
    stressButton.draw(screen, (0,0,0))
    strainButton.draw(screen, (0,0,0))
    # quizButton.draw(screen, (0,0,0))
    backButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if stressButton.isOver(pos):
                generalwindow_check.makeCurrent()
                stress_strain_window_check.endCurrent()
                stress_strain_win_select = [1,0]
                print(stress_strain_win_select)
                print("Entering in General strain Mode")
            if strainButton.isOver(pos):
                generalwindow_check.makeCurrent()
                stress_strain_window_check.endCurrent()
                stress_strain_win_select = [0,1]
                print(stress_strain_win_select)
                print("Entering in General strain Mode")
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                stress_strain_window_check.endCurrent()
        if event.type == pygame.MOUSEMOTION:
            if stressButton.isOver(pos):
                stressButton.color = (255, 0, 0)
            else:
                stressButton.color = (180, 0, 0)  
            if strainButton.isOver(pos):
                strainButton.color = (255, 0, 0)
            else:
                strainButton.color = (180, 0, 0) 
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

def gen2D_stress_input_window(screen, prev_win, windows): 
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_gen:"sigma_xx", sigma_yy_gen:"sigma_yy", sigma_xy_gen:"sigma_xy", angle_gen:"angle"}
    Small_font = game_font(20)
    head_text = Small_font.render("General 2- D Mode",1, (0,0,0))
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))
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
                gen2D_stress_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                try:
                    mohr_2d = Stress_MohrCircle(σxx= float(sigma_xx_gen.text), σyy= float(sigma_yy_gen.text),σzz= 0, 
                                                σxy= float(sigma_xy_gen.text), σyz=0, σzx=0)
                    mohr_2d.ndims = 2
                    mohr_2d.isGraph = True
                    if(angle_gen!=''):
                        mohr_2d.isAngle_stress = True
                        mohr_2d.reqAngle_stress_2d = float(angle_gen.text)
                    mohr_2d.stress_execute()
                    gen2D_stress_input_window_check.endCurrent()
                    gen2D_stress_input_window_check.makeCurrent()
                except:
                    gen2D_stress_input_window_check.endCurrent()
                    incompatible_input_window_check.makeCurrent()
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = True
                else:
                    box.active = False
        box_text_input(event, input_boxes)

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


def gen3D_stress_input_window(screen, prev_win, windows): 
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_gen:"sigma_xx", sigma_yy_gen:"sigma_yy", sigma_xy_gen:"sigma_xy", 
                   sigma_zz_gen:"sigma_zz", sigma_yz_gen:"sigma_yz", sigma_zx_gen:"sigma_zx",
                   angle1_gen:"Angle x", angle2_gen:'Angle y', angle3_gen:'Angle z'}
    Small_font = game_font(20)
    head_text = Small_font.render("General 3-D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))

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
                gen3D_stress_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_3d = Strain_MohrCircle(𝜏xx= float(sigma_xx_gen.text), 𝜏yy= float(sigma_yy_gen.text),𝜏zz= float(sigma_zz_gen.text), 
                                                𝜏xy= float(sigma_xy_gen.text), 𝜏yz= float(sigma_yz_gen.text),𝜏zx= float(sigma_zx_gen.text))
                    mohr_3d.ndims = 3
                    mohr_3d.isGraph = True
                    if(angle1_gen.text!='' and angle2_gen.text!= ''):
                        mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_gen.text))),3), 
                                                      round(np.cos(np.deg2rad(float(angle2_gen.text))),3), 0]
                        mohr_3d.isAngle_strain = True
                    mohr_3d.strain_execute()
                    gen3D_strain_input_window_check.endCurrent()
                    gen3D_strain_input_window_check.makeCurrent()
                except Exception as e:
                    print(e)
                    gen3D_stress_input_window_check.endCurrent()
                    incompatible_input_window_check.makeCurrent()                    
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = True
                else:
                    box.active = False
        box_text_input(event, input_boxes)


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

def gen2D_strain_input_window(screen, prev_win, windows): 
    clock = pygame.time.Clock()
    input_boxes = {tau_xx_gen:"tau_xx", tau_yy_gen:"tau_yy", tau_xy_gen:"tau_xy", angle_gen:"angle"}
    Small_font = game_font(20)
    head_text = Small_font.render("General 2- D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))

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
                gen2D_strain_input_window_check.endCurrent()
                # global s
                # s = s - 1
                # A.pop()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_2d = Strain_MohrCircle(𝜏xx= float(tau_xx_gen.text), 𝜏yy= float(tau_yy_gen.text),𝜏zz= 0, 
                                                𝜏xy= float(tau_xy_gen.text), 𝜏yz=0, 𝜏zx=0)
                    mohr_2d.ndims = 2
                    mohr_2d.isGraph = True
                    if(angle_gen!=''):
                        mohr_2d.isAngle_strain = True
                        mohr_2d.reqAngle_strain_2d = float(angle_gen.text)
                    mohr_2d.strain_execute()
                    gen2D_strain_input_window_check.endCurrent()
                    gen2D_strain_input_window_check.makeCurrent()
                except:
                    gen2D_strain_input_window_check.endCurrent()
                    incompatible_input_window_check.makeCurrent()
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = True
                else:
                    box.active = False
        box_text_input(event, input_boxes)


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


def gen3D_strain_input_window(screen, prev_win, windows): 
    clock = pygame.time.Clock()
    input_boxes = {tau_xx_gen:"tau_xx", tau_yy_gen:"tau_yy", tau_xy_gen:"tau_xy",
                   tau_zz_gen:"tau_zz", tau_yz_gen:"tau_yz", tau_zx_gen:"tau_zx",
                   angle1_gen:"Angle x", angle2_gen:'Angle y', angle3_gen:'Angle z'}
    Small_font = game_font(20)
    head_text = Small_font.render("General 3-D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))

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
                gen3D_strain_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_3d = Strain_MohrCircle(σxx= float(tau_xx_gen.text), σyy= float(tau_yy_gen.text),σzz= float(tau_zz_gen.text), 
                                                σxy= float(tau_xy_gen.text), σyz= float(tau_yz_gen.text),σzx= float(tau_zx_gen.text))
                    mohr_3d.ndims = 3
                    mohr_3d.isGraph = True
                    if(angle1_gen.text!='' and angle2_gen.text!= ''):
                        mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_gen.text))),3), 
                                                      round(np.cos(np.deg2rad(float(angle2_gen.text))),3), 0]
                        mohr_3d.isAngle_stress = True
                    mohr_3d.stress_execute()
                    gen3D_stress_input_window_check.endCurrent()
                    gen3D_stress_input_window_check.makeCurrent()
                except:
                    gen3D_strain_input_window_check.endCurrent()
                    incompatible_input_window_check.makeCurrent()                    
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = True
                else:
                    box.active = False
        box_text_input(event, input_boxes)


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