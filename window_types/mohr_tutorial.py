import pygame
import numpy as np
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
import random
from utilities.mohr_screen import *
from MohrCircle_stress import Stress_MohrCircle
from MohrCircle_strain import Strain_MohrCircle
# from MohrCircle_strain import strain_execute
angle_check = 0
stress_strain_win_select = [0,0]
def tutorialwindow(screen, prev_win, windows):
    Small_font = game_font(20)
    text = Small_font.render("Tutorial Mode",1, (0,0,0))
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
                    tut2D_stress_input_window_check.makeCurrent()
                    tutorialwindow_check.endCurrent()
                    print("Entering in stress 2-D Mode")
            if threedButton.isOver(pos):
                if(stress_strain_win_select[0]==1):
                    tut3D_stress_input_window_check.makeCurrent()
                    tutorialwindow_check.endCurrent()
                    print("Entering in 3-D Mode")
                else:
                    tut3D_strain_input_window_check.makeCurrent()
                    tutorialwindow_check.endCurrent()
                    print("Entering in strain 2-D Mode")
            if backButton.isOver(pos):
                tut_stress_strain_window_check.makeCurrent()
                tutorialwindow_check.endCurrent()

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

def tut_stress_strain_window(screen, prev_win, windows):
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
                tutorialwindow_check.makeCurrent()
                tut_stress_strain_window_check.endCurrent()
                stress_strain_win_select = [1,0]
                print(stress_strain_win_select)
                print("Entering in Tutorial strain Mode")
            if strainButton.isOver(pos):
                tutorialwindow_check.makeCurrent()
                tut_stress_strain_window_check.endCurrent()
                stress_strain_win_select = [0,1]
                print(stress_strain_win_select)
                print("Entering in Tutorial strain Mode")
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                tut_stress_strain_window_check.endCurrent()
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

def tut2D_step1_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-1",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["The first step to draw a 2-d Mohr circle ",
              "for the given stress state is to draw",
              "the points corresponding to the stresses" ,
              "On a graph, Plot: ",
              "(sigma_xx, -tau_xy) & (sigma_yy, tau_xy)"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(120, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_stress_input_window_check.makeCurrent()
                tut2D_step1_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut2D_step1_window_check.endCurrent()
                tut2D_step2_window_check.makeCurrent()

def tut2D_step2_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-2",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["The next step to draw a 2-d Mohr circle ",
              "for the given stress state is to draw",
              "is to join the points plotted using a ",
              "straight line. Mark the point where the ",
              "line intersects X-axis as the centre of ",
              "the circle" ,]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(120, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step1_window_check.makeCurrent()
                tut2D_step2_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut2D_step2_window_check.endCurrent()
                tut2D_step3_window_check.makeCurrent()
def tut2D_step3_window(screen, prev_win, windows):
    global angle_check
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-3",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the centre and radius being ",
              "the distance between the centre and one ",
              "of the plotted points, draw a circle.",
              "Thus you get your Mohr's Circle"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(120, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    xButton = nextButton
    if angle_check==0:
        xButton = finishButton
    xButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step2_window_check.makeCurrent()
                tut2D_step3_window_check.endCurrent()
            if xButton.isOver(pos):
                if xButton==nextButton:
                    tut2D_step3_window_check.endCurrent()
                    tut2D_step4_window_check.makeCurrent()
                else:
                    tut2D_step3_window_check.endCurrent()
                    tut2D_final_window_check.makeCurrent()
def tut2D_step4_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-4",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the centre and radius being ",
              "To find the values of stress at an angle", 
              "say theta. Rotate the line about the centre",
              "by an angle of 2*theta.", " ",
              "NOTE: the rotation should be in anticlockwise ",
              "direction with the angle is positive and",
              "clockwise if the angle is negative"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(120, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step3_window_check.makeCurrent()
                tut2D_step4_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut2D_step5_window_check.makeCurrent()
                tut2D_step4_window_check.endCurrent()
def tut2D_step5_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-5",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the centre and radius being ",
              "Thus the new line has its end-points on",
              "the circle. These endpoints denote the new",
              "(sigma_xx, -tau_xy) and (sigma_yy, tau_xy)",
              " ",
              "Thus you get the required values of stress",
              "at the required angle using Mohr's Circle!!!"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(120, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    finishButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step4_window_check.makeCurrent()
                tut2D_step5_window_check.endCurrent()
            if finishButton.isOver(pos):
                tut2D_final_window_check.makeCurrent()
                tut2D_step5_window_check.endCurrent()

def tut2D_final_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("Congratulations!!",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the centre and radius being ",
              "you have learnt to draw a Mohr Circle",
              "and find the component of stress at various",
              "angles.",
              "Try out the Quiz! or Explore in General Mode"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(120, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    back_to_homeButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                windows[prev_win][1].makeCurrent()
                tut2D_final_window_check.endCurrent()
            if back_to_homeButton.isOver(pos):
                enterWindow_check.makeCurrent()
                tut2D_final_window_check.endCurrent()
def tut2D_stress_input_window(screen, prev_win, windows): 
    global angle_check
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_tut:"sigma_xx", sigma_yy_tut:"sigma_yy", tau_xy_tut:"tau_xy", angle_tut:"angle"}
    Small_font = game_font(20)
    head_text = Small_font.render("Tutorial 2- D Mode",1, (0,0,0))
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))
    screen.blit(head_text, (360, 100))  
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tutorialwindow_check.makeCurrent()
                tut2D_stress_input_window_check.endCurrent()
            if nextButton.isOver(pos):
                try:
                    mohr_2d = Stress_MohrCircle(σxx= float(sigma_xx_tut.text), σyy= float(sigma_yy_tut.text),σzz= 0, 
                                                σxy= float(tau_xy_tut.text), σyz=0, σzx=0)
                    mohr_2d.ndims = 2
                    mohr_2d.isGraph = False
                    if(angle_tut.text!=''):
                        mohr_2d.isAngle_stress = True
                        angle_check = 1
                        mohr_2d.reqAngle_stress_2d = float(angle_tut.text)
                    else:
                        angle_check = 0
                    mohr_2d.stress_execute()
                    tut2D_stress_input_window_check.endCurrent()
                    tut2D_step1_window_check.makeCurrent()
                except:
                    tut2D_stress_input_window_check.endCurrent()
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


def tut3D_stress_input_window(screen, prev_win, windows): 
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_tut:"sigma_xx", sigma_yy_tut:"sigma_yy", tau_xy_tut:"tau_xy", 
                   sigma_zz_tut:"sigma_zz", tau_yz_tut:"tau_yz", tau_zx_tut:"tau_zx",
                   angle1_tut:"Angle x", angle2_tut:'Angle y', angle3_tut:'Angle z'}
    Small_font = game_font(20)
    head_text = Small_font.render("Tutorial 3-D Mode",1, (0,0,0))
    
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
                tutorialwindow_check.makeCurrent()
                tut3D_stress_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_3d = Strain_MohrCircle(𝜏xx= float(sigma_xx_tut.text), 𝜏yy= float(sigma_yy_tut.text),𝜏zz= float(sigma_zz_tut.text), 
                                                𝜏xy= float(tau_xy_tut.text), 𝜏yz= float(tau_yz_tut.text),𝜏zx= float(tau_zx_tut.text))
                    mohr_3d.ndims = 3
                    mohr_3d.isGraph = True
                    if(angle1_tut.text!='' and angle2_tut.text!= ''):
                        mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_tut.text))),3), 
                                                      round(np.cos(np.deg2rad(float(angle2_tut.text))),3), 0]
                        mohr_3d.isAngle_strain = True
                    mohr_3d.strain_execute()
                    tut3D_strain_input_window_check.endCurrent()
                    tut3D_strain_input_window_check.makeCurrent()
                except Exception as e:
                    print(e)
                    tut3D_stress_input_window_check.endCurrent()
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

def tut2D_strain_input_window(screen, prev_win, windows): 
    clock = pygame.time.Clock()
    input_boxes = {epsi_xx_tut:"epsi_xx", epsi_yy_tut:"epsi_yy", epsi_xy_tut:"epsi_xy", angle_tut:"angle"}
    Small_font = game_font(20)
    head_text = Small_font.render("Tutorial 2- D Mode",1, (0,0,0))
    
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
                tutorialwindow_check.makeCurrent()
                tut2D_strain_input_window_check.endCurrent()
                # global s
                # s = s - 1
                # A.pop()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_2d = Strain_MohrCircle(𝜏xx= float(epsi_xx_tut.text), 𝜏yy= float(epsi_yy_tut.text),𝜏zz= 0, 
                                                𝜏xy= float(epsi_xy_tut.text), 𝜏yz=0, 𝜏zx=0)
                    mohr_2d.ndims = 2
                    mohr_2d.isGraph = True
                    if(angle_tut!=''):
                        mohr_2d.isAngle_strain = True
                        mohr_2d.reqAngle_strain_2d = float(angle_tut.text)
                    mohr_2d.strain_execute()
                    tut2D_strain_input_window_check.endCurrent()
                    tut2D_strain_input_window_check.makeCurrent()
                except:
                    tut2D_strain_input_window_check.endCurrent()
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


def tut3D_strain_input_window(screen, prev_win, windows): 
    clock = pygame.time.Clock()
    input_boxes = {epsi_xx_tut:"epsi_xx", epsi_yy_tut:"epsi_yy", epsi_xy_tut:"epsi_xy",
                   epsi_zz_tut:"epsi_zz", epsi_yz_tut:"epsi_yz", epsi_zx_tut:"epsi_zx",
                   angle1_tut:"Angle x", angle2_tut:'Angle y', angle3_tut:'Angle z'}
    Small_font = game_font(20)
    head_text = Small_font.render("Tutorial 3-D Mode",1, (0,0,0))
    
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
                tutorialwindow_check.makeCurrent()
                tut3D_strain_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_3d = Strain_MohrCircle(σxx= float(epsi_xx_tut.text), σyy= float(epsi_yy_tut.text),σzz= float(epsi_zz_tut.text), 
                                                σxy= float(epsi_xy_tut.text), σyz= float(epsi_yz_tut.text),σzx= float(epsi_zx_tut.text))
                    mohr_3d.ndims = 3
                    mohr_3d.isGraph = True
                    if(angle1_tut.text!='' and angle2_tut.text!= ''):
                        mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_tut.text))),3), 
                                                      round(np.cos(np.deg2rad(float(angle2_tut.text))),3), 0]
                        mohr_3d.isAngle_stress = True
                    mohr_3d.stress_execute()
                    tut3D_stress_input_window_check.endCurrent()
                    tut3D_stress_input_window_check.makeCurrent()
                except:
                    tut3D_strain_input_window_check.endCurrent()
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