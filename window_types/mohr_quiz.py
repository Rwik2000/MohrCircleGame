
import pygame
import numpy as np
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
from MohrCircle_new import execute
import random
from utilities.mohr_screen import *
import time

quiz_question_type = ['2-D', '2-D', '3-D', '3-D','concept']
# def game_font(size):
#     return(pygame.font.Font('Fonts/pt mono regular.ttf', size))
def quizwindow(screen):
    Small_font = game_font(20)
    text = Small_font.render("Quiz Mode",1, (0,0,0))
    screen.blit(text, (360, 100))
    backButton.draw(screen, (0,0,0))
    startButton.draw(screen,(0,0,0))

    global quiz_question_type, sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_yz, sigma_zx
    # print(len(quiz_question_type))
    random.shuffle(quiz_question_type)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                quizwindow_check.endCurrent()

            if startButton.isOver(pos):
                if quiz_question_type[0] == '2-D':
                    sigma_xx = round(random.uniform(1,30), 2)
                    sigma_yy = round(random.uniform(1,30), 2)
                    sigma_xy = round(random.uniform(1,30), 2)
                    quiz_question_type = quiz_question_type[1:]
                    quizwindow_2d_check.makeCurrent()
                    quizwindow_check.endCurrent()
                elif quiz_question_type[0] == '3-D':
                    sigma_xx = round(random.uniform(1,30), 2)
                    sigma_yy = round(random.uniform(1,30), 2)
                    sigma_zz = round(random.uniform(1,30), 2)
                    sigma_xy = round(random.uniform(1,30), 2)
                    sigma_yz = round(random.uniform(1,30), 2)
                    sigma_zx = round(random.uniform(1,30), 2)
                    quiz_question_type = quiz_question_type[1:]
                    quizwindow_3d_check.makeCurrent()
                    quizwindow_check.endCurrent()
                elif quiz_question_type[0] == 'Concept':   
                    quiz_question_type = quiz_question_type[1:]
                    quizwindow_concept_check.makeCurrent()
                    quizwindow_check.endCurrent()
                

        if event.type == pygame.MOUSEMOTION:
            if startButton.isOver(pos):
                startButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

def quiz_button_loop(event, x_button, current_window_check, ans_box, curr_question_type):
    Small_font = game_font(20)
    global quiz_question_type,sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_yz, sigma_zx
    pos = pygame.mouse.get_pos()

    if event.type == pygame.QUIT:  
        global running              
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        
        if x_button.isOver(pos):
            if curr_question_type!='concept':
                if curr_question_type=='2-D':
                    mohrCircle_input = [sigma_xx,sigma_yy,sigma_xy, 0,0,0]

                    execute(2,mohrCircle_input)
                elif curr_question_type=='3-D':
                    mohrCircle_input = [sigma_xx,sigma_yy,sigma_xy,sigma_zz,sigma_yz,sigma_zx]

                execute(3,mohrCircle_input)
            sigma_xx,sigma_yy,sigma_xy,sigma_zz,sigma_yz,sigma_zx = None,None,None,None,None,None
            if len(quiz_question_type) > 0:
                if quiz_question_type[0] == '2-D':
                    sigma_xx = round(random.uniform(1,30), 2)
                    sigma_yy = round(random.uniform(1,30), 2)
                    sigma_xy = round(random.uniform(1,30), 2)
                    quiz_question_type = quiz_question_type[1:]
                    current_window_check.endCurrent()
                    quizwindow_2d_check.makeCurrent()    
                elif quiz_question_type[0] == '3-D':
                    sigma_xx = round(random.uniform(1,30), 2)
                    sigma_yy = round(random.uniform(1,30), 2)
                    sigma_zz = round(random.uniform(1,30), 2)
                    sigma_xy = round(random.uniform(1,30), 2)
                    sigma_yz = round(random.uniform(1,30), 2)
                    sigma_zx = round(random.uniform(1,30), 2)
                    quiz_question_type = quiz_question_type[1:]
                    current_window_check.endCurrent()
                    quizwindow_3d_check.makeCurrent()
                elif quiz_question_type[0] == 'Concept':   
                    quiz_question_type = quiz_question_type[1:]
                    current_window_check.endCurrent()
                    quizwindow_concept_check.makeCurrent()
            else:
                current_window_check.endCurrent()
                quiz_end_window_check.makeCurrent()
        for box in ans_box.keys():
            if box.render().collidepoint(event.pos):
                # print("click")
                box.active = True
            else:
                box.active = False
    if event.type == pygame.KEYDOWN:
        for box in ans_box.keys():
            if box.active:
                if event.key == pygame.K_RETURN:
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
    if event.type == pygame.MOUSEMOTION:
        if x_button.isOver(pos):
            x_button.color = (255, 0, 0)
        else:
            x_button.color = (180, 0, 0)
    return ans_box 

def quizwindow_2d(screen):
    clock = pygame.time.Clock()
    Big_font = game_font(40)
    Small_font = game_font(20)
    text = Big_font.render("Quiz on 2-D Mohr circle",1, (0,0,0))
    screen.blit(text, (100, 70))
    text = Small_font.render("Draw the mohr circle for the following 2-D stress field",1, (0,0,0))
    screen.blit(text, (30, 150))

    ans_boxes_2d = {C1_gen:"C1"}
    for box in ans_boxes_2d.keys():
        box_text = Small_font.render(ans_boxes_2d[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 80, box.y))

    curr_question_type = '2-D'
    global quiz_question_type,sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_yz, sigma_zx
    # print(len(quiz_question_type))

    text = Small_font.render("sigma_xx = ",1, (0,0,0))
    screen.blit(text, (50, 200))
    text = Small_font.render("sigma_yy = ",1, (0,0,0))
    screen.blit(text, (50, 250))
    text = Small_font.render("sigma_xy = ",1, (0,0,0))
    screen.blit(text, (50, 300))

    text = Small_font.render(str(sigma_xx) , 1, (0,0,0))
    screen.blit(text, (180, 200))
    text = Small_font.render(str(sigma_yy) ,1, (0,0,0))
    screen.blit(text, (180, 250))
    text = Small_font.render(str(sigma_xy) ,1, (0,0,0))
    screen.blit(text, (180, 300))

    x_button = nextButton
    if len(quiz_question_type) == 0:
        x_button = submitButton
    x_button.draw(screen, (0,0,0))

    for event in pygame.event.get():
        ans_boxes_2d=quiz_button_loop(event, x_button, quizwindow_2d_check, ans_boxes_2d, curr_question_type)
          

    for box in ans_boxes_2d.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)

def quizwindow_3d(screen):
    clock = pygame.time.Clock()
    Big_font = game_font(40)
    Small_font = game_font(20)
    text = Big_font.render("Quiz on 3-D Mohr circle",1, (0,0,0))
    screen.blit(text, (100, 70))
    text = Small_font.render("Draw the mohr circle for the following 3-D stress field",1, (0,0,0))
    screen.blit(text, (30, 150))

    ans_boxes_3d = {C1_gen:"C1", C2_gen:"C2", C3_gen:"C3"}
    for box in ans_boxes_3d.keys():
        box_text = Small_font.render(ans_boxes_3d[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 80, box.y))

    curr_question_type = '3-D'
    global quiz_question_type,sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_yz, sigma_zx
    # print(len(quiz_question_type))

    text = Small_font.render("sigma_xx = ",1, (0,0,0))
    screen.blit(text, (50, 200))
    text = Small_font.render("sigma_yy = ",1, (0,0,0))
    screen.blit(text, (50, 250))
    text = Small_font.render("sigma_zz = ",1, (0,0,0))
    screen.blit(text, (50, 300))
    text = Small_font.render("sigma_xy = ",1, (0,0,0))
    screen.blit(text, (50, 350))
    text = Small_font.render("sigma_yz = ",1, (0,0,0))
    screen.blit(text, (50, 400))
    text = Small_font.render("sigma_zx = ",1, (0,0,0))
    screen.blit(text, (50, 450))

    text = Small_font.render(str(sigma_xx) , 1, (0,0,0))
    screen.blit(text, (180, 200))
    text = Small_font.render(str(sigma_yy) ,1, (0,0,0))
    screen.blit(text, (180, 250))
    text = Small_font.render(str(sigma_zz) ,1, (0,0,0))
    screen.blit(text, (180, 300))
    text = Small_font.render(str(sigma_xy) ,1, (0,0,0))
    screen.blit(text, (180, 350))
    text = Small_font.render(str(sigma_yz) ,1, (0,0,0))
    screen.blit(text, (180, 400))
    text = Small_font.render(str(sigma_zx) ,1, (0,0,0))
    screen.blit(text, (180, 450))

    x_button = nextButton
    if len(quiz_question_type) == 0:
        x_button = submitButton
    x_button.draw(screen, (0,0,0))

    for event in pygame.event.get():
        ans_boxes_3d = quiz_button_loop(event, x_button, quizwindow_3d_check, ans_boxes_3d,curr_question_type)
        
    for box in ans_boxes_3d.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)

def quizwindow_concept(screen):
    global quiz_question_type,sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_yz, sigma_zx
    # print(len(quiz_question_type))

    x_button = nextButton
    if len(quiz_question_type) == 0:
        x_button = submitButton
    x_button.draw(screen, (0,0,0))

    curr_question_type = 'concept'
    for event in pygame.event.get():
        quiz_button_loop(event, x_button, quizwindow_concept_check, {},curr_question_type)

def quiz_end_window(screen):
    Big_font = game_font(80)
    Small_font = game_font(20)
    text = Big_font.render("Quiz Over", 1, (0,0,0))
    screen.blit(text, (70, 250))
    text = Small_font.render ("Please proceed to get your Scores!!",1, (0,0,0))
    screen.blit(text, (60, 400))
    enterButton.draw(screen, (0,0,0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False

        if event.type == pygame.MOUSEMOTION:
            if enterButton.isOver(pos):
                enterButton.color = (255, 0, 0)
            else:
                enterButton.color = (180, 0, 0)
    