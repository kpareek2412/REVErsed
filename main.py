

from random import randint
from turtle import pos

import pymunk
import math
import time
import pygame 
import sprite_sheet
from pygame import K_RETURN, mixer
import os


pygame.init()



clock = pygame.time.Clock()

if(not os.path.exists("hiscore.txt")):
    with open("hiscore.txt", "w") as f:
        f.write("0")

text01 = '''  Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Try the new cross-platform PowerShell https://aka.ms/pscore6'''

text_0 = '''  Studio Head of Mojang Studios
Helen Chiang
Head of Stockholm Studios
Ulrika Höjgård
Design
Chief Creative Officers
Jens Bergensten'''

text_1 = '''  Game Directors
Agnes Larsson
 Måns Olson
 Creative Directors
 Jesse Merriam
Magnus Nedfors Torfi Frans Olafsson'''

text_2 = '''   Principal Design Director
Craig Leigh-Design Manager
Michael Harnisch,Lead Game Designers
 Rob Poerschke
 Robin V Vincent
 Game Designers'''

text_3 = '''   Art Usher
 Brandon Pearce
 Christian Berg
 Cole Phillips
Cory Scheviak
Henrik Kniberg
Laura de Llorens Garcia'''

text_4 = '''   #Matthew Gatland 
michael Stagnitta
Nir Vaknin
 Steve Enos
 Tod Pang
 Narrative Director
 Kevin Grace'''

text_5 = '''  Narrative Designers
Kelsey Howard
Design Manager
Rabi Afram
 Programming'''

text_6 = '''
  Chief Technology Officer
Michael W Weilbacher
Head of Services and Ops Engineering
Vince Curley
'''

text_7 = '''   Jason Cahill
Director of Franchise Quality
Matthew Ng
Technical Director
Christopher Östlund
Daniel Johansson
Jeff McKune'''

text_8 = '''  Jifeng Zhang
Lawrence M. Sanchez II
Michael J. Ott
Nathan Adams
Lead Game Developers
Andrew Maher
Gary McLaughlin'''

text_9 = '''  Geoff Ebersol
Henning Erlandsen
Jakob Ryden
James S Yarrow
Mason McCuskey
Matt Hawley
Michael Scott'''

text_10 = '''  Mikael Hedberg
Torbjörn Allard
Game Developers
Alex Couch (Insight Global, Inc)
'''

text_11 = '''  Head of Game Engineering
Åsa Bredin
Head of Creator Platform Engineering
Alexander Sandor
Alexander Torstling
'''

text_12 = '''  Brian Threvathan
Chad George
Cody Centers (Insight Global, Inc)
Daniel Brynolf
Daniel Lobo
David Dalström
Erik Broes'''

text_13 = '''  Ethan A Hall (Collabera)
Felix JonesAdrian Toncean
Alex Green (Red Lens Games, Inc)
Alexander Östman'''

text_14='''  # Fredrik Bergstrand
Georgii Gavrichev
Harald Johansson'''

text_15 = '''  Aron Nieminen
Bartosz Bok
Benny Hellström
Billy Sjöberg
Bjarni Gudmundsson'''



        
def getimg(img , frame, width , height, scale, colour):
    img_scr_png = pygame.image.load(img)
    img_img = sprite_sheet.Spritesheet(img_scr_png)
    img_ = img_img.get_img(frame,width,height,scale,colour)

    return img_








def blit_(screen,img, x,y):
    x = screen.blit(img,(x,y))
    return x


font = pygame.font.Font(None, 17)
font_ = pygame.font.Font(None,200)
font_hw = pygame.font.Font("Python/Games/reversed/Fonts/James Fajardo.ttf", 1500)
font_sg = pygame.font.Font("Python/Games/reversed/Fonts/Game Of Squids.otf", 10)
font_p = pygame.font.Font("Python/Games/reversed/Fonts/Kapel.ttf", 90)
font_p_ = pygame.font.Font("Python/Games/reversed/Fonts/Kapel.ttf", 40)

def font_render(fontx,screenx,textx,color,x,y):
    screen_text = fontx.render(textx,True,color)
    screenx.blit(screen_text,(x,y))







pygame.init()

 # Game specific variables
end_game = False
game_over = False

BG = (0,0,0)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
zhut_clr = (136,136,136)
scr_width = 800
scr_height = 500
lbat_x=0
lbat_y=0
rbat_x=754
rbat_y=0
zhut_x = 100
zhut_y = 215    

lbat_v = 300
rbat_v = 300

fps = 60




# Getting the sprite
sprite_img = pygame.image.load("Python/Games/reversed/images/bat.png")
sprite = sprite_sheet.Spritesheet(sprite_img)

frame_0 = sprite.get_img(0,100,160, 0.4,white)
frame_1 = sprite.get_img(0,100,160, 0.4,white)






screen = pygame.display.set_mode((scr_width,scr_height))
pygame.display.set_caption('REVErsed')










def one_v_one():
    game_over = False


    end_game = False
    game_over = False

    BG = (0,0,0)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    scor_clr = (10,10,10)
    scr_width = 800
    scr_height = 500
    lbat_x=0
    lbat_y=0
    rbat_x=754
    rbat_y=0

    ball_x = 40
    ball_y = 30
        

    lbat_v = 0
    rbat_v = 0

    ball_v = 0

    fps = 60

    score_r = 0
    score = 0
    font_x = 180

    fontr_x = 560



    # Getting the sprite
    sprite_img = pygame.image.load("Python/Games/reversed/images/bat.png")
    sprite = sprite_sheet.Spritesheet(sprite_img)
    frame_0 = sprite.get_img(0,100,160, 0.4,white)
    frame_1 = sprite.get_img(0,100,160, 0.4,white)

    ball_img_png = pygame.image.load("Python/Games/reversed/images/ball.png")
    ball_img = sprite_sheet.Spritesheet(ball_img_png)
    ball = ball_img.get_img(0,30,30,0.7,white)         
    ball_vx =  5.892556509887834
    ball_vy = 5.892556509887834 
    x =0
    y = 0

    onevone = pygame.image.load("Python/Games/reversed/images/1v1.png")


    defeat = mixer.Sound("Python/Games/reversed/audio/Defeat.wav")
    




    





    while not end_game:


 



    
        while not game_over:

            x+= 1
           
            
            hit = mixer.Sound("Python/Games/reversed/audio/hit.wav")
            
    

                
            screen.fill(BG)
            blit_(screen,onevone,0,0)
            font_render(font_,screen,str(score),scor_clr,font_x,190)
            font_render(font_,screen,str(score_r), scor_clr,fontr_x , 190)
            blit_(screen,frame_1,rbat_x,rbat_y)

            blit_(screen,frame_0,lbat_x,lbat_y)  

            blit_(screen,ball,ball_x,ball_y) 
            

            if lbat_y >= 430 :
                lbat_y = 430

            if lbat_y <=5:
                lbat_y = 5

            if rbat_y >= 430 :
                rbat_y = 430

            if rbat_y <=5:
                rbat_y = 5

            

                



     

 
            if x >= 60:

                if lbat_x<=ball_x <= (lbat_x+35)  and lbat_y<= ball_y<= (lbat_y+100):
                    score += 1
                    x =0
                    ball_vx = ball_vx*(-1)
                    hit.play()

                


                elif ball_x>= (rbat_x-5) and rbat_y<= ball_y <= (rbat_y+133):
                    x = 0
                    ball_vx = ball_vx*(-1)
                    score_r += 1
                    hit.play()


            if ball_y < 10 or ball_y > 470:
                ball_vy = ball_vy*(-1)


            if ball_x <= 5 or ball_x >= 795:
                game_over = True


            

            
                



            for event in pygame.event.get():



                if event.type == pygame.QUIT:
            
 
                    pygame.quit()
                    quit()
                        
                        

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        lbat_v -= 10

                    if event.key == pygame.K_s:
                        lbat_v += 10

                    if event.key == pygame.K_UP:
                        rbat_v -= 10

                    if event.key == pygame.K_DOWN:
                        rbat_v += 10

           

                                            




                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        rbat_v = 0
            

                    elif event.key == pygame.K_w or event.key == pygame.K_s:
                        lbat_v = 0



            lbat_y += lbat_v
            rbat_y += rbat_v

            ball_x += ball_vx
            ball_y += ball_vy 

         

                            


        
            pygame.display.update()

                


            clock.tick(fps)  
       
       
        y += 1
 
        if y == 1:
            defeat.play()

        gameover1v1(score,score_r)


    
    pygame.quit()
    quit()


def mentos_zindagi():
    game_over = False


    end_game = False
    game_over = False

    BG = (0,0,0)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    scor_clr = (10,10,10)
    scr_width = 800
    scr_height = 500
    lbat_x=0
    lbat_y=0
    rbat_x=754
    rbat_y=0

    ball_x = 395
    ball_y = 245
        

    lbat_v = 500
    rbat_v = 300
    ball_v = 0

    

    ball_v = 0

    lb_y = randint(0,500)
    rb_y = randint(0,500)

    fps = 60
    global score_mg
    score_mg = 0
    font_x = 365




    # Getting the sprite
    sprite_img = pygame.image.load("Python/Games/reversed/images/bat.png")
    sprite = sprite_sheet.Spritesheet(sprite_img)
    frame_0 = sprite.get_img(0,100,160, 0.4,white)
    frame_1 = sprite.get_img(0,100,160, 0.4,white)

    ball_img_png = pygame.image.load("Python/Games/reversed/images/ball.png")
    ball_img = sprite_sheet.Spritesheet(ball_img_png)
    ball = ball_img.get_img(0,30,30,0.7,white)         
    ball_vx =  4.892556509887834
    ball_vy = 0


    x =0
    y = 0
    r = 0
    


    defeat = mixer.Sound("Python/Games/reversed/audio/Defeat.wav")
    




    





    while not end_game:
        if(not os.path.exists("hiscore_mg.txt")):
            with open("hiscore_mg.txt", "w") as k:
                k.write("0")

        with open("hiscore_mg.txt", "r") as k:
            global hiscore_mg
            hiscore_mg = k.read()
 



    
        while not game_over:


            x+= 1
            r += 1
 


            #     if lb_y >= 250:
            #         lb_y = randint(0,250)

            #     elif lb_y < 250:
            #         lb_y = randint(250,500)

            #     if rb_y >= 250:

            #         rb_y = randint(0,250)

            #     elif rb_y < 250:
            #         rb_y = randint(250,500)

            #     r = 0

            # del_lb_y = lb_y - lbat_y
            # del_rb_y = rb_y - rbat_y

          
           
            
            hit = mixer.Sound("Python/Games/reversed/audio/hit.wav")

            if lbat_y > 440 :
                lbat_v = -500

            elif lbat_y <= 5:
                lbat_v = 500

            if rbat_y > 440 :
                rbat_v = - 300

            elif rbat_y <= 5:
                rbat_v = 300
            


                
            screen.fill(BG)
            font_render(font_,screen,str(score_mg),scor_clr,font_x,190)
            blit_(screen,frame_0,rbat_x,rbat_y)

            blit_(screen,frame_0,lbat_x,lbat_y)  

            blit_(screen,ball,ball_x,ball_y) 



            

                

            if score_mg >= 10:
                font_x = 340

            if score_mg > int(hiscore_mg):
                hiscore_mg = score_mg


 
            if x >= 60:

                if (lbat_x<=ball_x <= (lbat_x+35)  and lbat_y<= ball_y<= (lbat_y+90)) or (rbat_x-5<= ball_x <= (rbat_x+35) and rbat_y <= ball_y <= (rbat_y+123)) :
                    score_mg += 1
                    x =0
                    ball_vx = ball_vx*(-1)
                    hit.play()


           


            if ball_y <= 10 :
                ball_y = 10

            if ball_y >= 470:
                ball_y = 470


            if ball_x <= 5 or ball_x >= 795:
                game_over = True


            

            
                



            for event in pygame.event.get():



                if event.type == pygame.QUIT:
                    with open("hiscore.txt", "r") as f:
                        hiscore_mg = f.read()
 
                    pygame.quit()
                    quit()
                        
                        

                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_w or event.key == pygame.K_UP:
                        ball_vy = -10
                                
                    if  event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        ball_vy = 10

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP or event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        ball_vy = 0

                
                        

                        

                                            






            ball_x += ball_vx
            ball_y += ball_vy 


            lbat_y += lbat_v/60
            rbat_y += rbat_v/60

         

                            


        
            pygame.display.update()

                


            clock.tick(fps)  
       
       
        y += 1
        with open("hiscore.txt", "w") as f:
            f.write(str(hiscore_mg))
        if y == 1:
            defeat.play()

        gameover(score_mg,hiscore_mg,'mentos_zindagi')


    
    pygame.quit()
    quit()

    
    
def aam_zinagi():
    game_over = False


    end_game = False
    game_over = False

    BG = (0,0,0)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    scor_clr = (10,10,10)
    scr_width = 800
    scr_height = 500
    lbat_x=0
    lbat_y=0
    rbat_x=754
    rbat_y=0

    ball_x = 40
    ball_y = 30
        

    lbat_v = 0
    rbat_v = 0

    ball_v = 0

    fps = 60
    global score
    score = 0
    font_x = 365




    # Getting the sprite
    sprite_img = pygame.image.load("Python/Games/reversed/images/bat.png")
    sprite = sprite_sheet.Spritesheet(sprite_img)
    frame_0 = sprite.get_img(0,100,160, 0.4,white)
    frame_1 = sprite.get_img(0,100,160, 0.4,white)

    ball_img_png = pygame.image.load("Python/Games/reversed/images/ball.png")
    ball_img = sprite_sheet.Spritesheet(ball_img_png)
    ball = ball_img.get_img(0,30,30,0.7,white)         
    ball_vx =  5.892556509887834
    ball_vy = 5.892556509887834 
    x =0
    y = 0


    defeat = mixer.Sound("Python/Games/reversed/audio/Defeat.wav")
    




    





    while not end_game:
        if(not os.path.exists("hiscore.txt")):
            with open("hiscore.txt", "w") as f:
                f.write("0")

        with open("hiscore.txt", "r") as f:
            global hiscore
            hiscore = f.read()
 



    
        while not game_over:

            x+= 1
           
            
            hit = mixer.Sound("Python/Games/reversed/audio/hit.wav")
            
            rbat_y = ball_y
            #275 - 228


                
            screen.fill(BG)
            font_render(font_,screen,str(score),scor_clr,font_x,190)
            blit_(screen,frame_1,rbat_x,rbat_y)

            blit_(screen,frame_0,lbat_x,lbat_y)  

            blit_(screen,ball,ball_x,ball_y) 

            if lbat_y >= 430 :
                lbat_y = 430

            if lbat_y <=5:
                lbat_y = 5

            if rbat_y >= 430 :
                rbat_y = 430

            if rbat_y <=5:
                rbat_y = 5

            

                

            if score >= 10:
                font_x = 340

            if score > int(hiscore):
                hiscore = score


 
            if x >= 120:

                if lbat_x<=ball_x <= (lbat_x+35)  and lbat_y<= ball_y<= (lbat_y+100):
                    score += 1
                    x =0
                    ball_vx = ball_vx*(-1)
                    hit.play()


            if ball_x>= (rbat_x-5) and rbat_v<= ball_y <= (rbat_y+133):
                ball_vx = ball_vx*(-1)
                hit.play()


            if ball_y < 10 or ball_y > 470:
                ball_vy = ball_vy*(-1)


            if ball_x <= 5 or ball_x >= 795:
                game_over = True


            

            
                



            for event in pygame.event.get():



                if event.type == pygame.QUIT:
                    with open("hiscore.txt", "r") as f:
                        hiscore = f.read()
 
                    pygame.quit()
                    quit()
                        
                        

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                            lbat_v -= 10
                                
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        lbat_v += 10 

                                            




                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                            lbat_v = 0

                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        lbat_v = 0



            lbat_y += lbat_v

            ball_x += ball_vx
            ball_y += ball_vy 

         

                            


        
            pygame.display.update()

                


            clock.tick(fps)  
       
       
        y += 1
        with open("hiscore.txt", "w") as f:
            f.write(str(hiscore))
        if y == 1:
            defeat.play()

        gameover(score,hiscore,'aam_zinagi')


    
    pygame.quit()
    quit()


def gameover(scre,h_scre, loop):
    gm_ov_clr = (102,102,102)
    ball_img_png = pygame.image.load("Python/Games/reversed/images/ball.png")
    gmove_scr = pygame.image.load("Python/Games/reversed/images/Game_over_scrn.png")

    click_sound = mixer.Sound("Python/Games/reversed/audio/click.wav")
    ball_img = sprite_sheet.Spritesheet(ball_img_png)
    ball = ball_img.get_img(0,30,30,0.7,white) 
    no_pg = 0
    no_e = 0
    no_m = 0
    x_pg = 0
    x_e = 0
    x_m = 0

    end_game = False
    while not end_game:
        pos = pygame.mouse.get_pos()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
        play_ag = getimg("Python/Games/reversed/images/playag_script.png", no_pg,175, 60,1.7,black )
        exit = getimg("Python/Games/reversed/images/exit.png", no_e , 175,60,1,black)
        menu = getimg("Python/Games/reversed/images/menu_but.png", no_m,175,60,0.7,black)
        screen.fill(BG)
        blit_(screen,gmove_scr,0,0)
        blit_(screen,frame_0,lbat_x,lbat_y)
        blit_(screen,frame_1,rbat_x,rbat_y)    #509 335, 579 359
        blit_(screen,play_ag,160,320)
        blit_(screen,exit,460,320)
        blit_(screen,menu,490,370)
        font_render(font_p_,screen,'SCORE ->' + str(scre), (0,150,255), 350,235)
        font_render(font_p_, screen, "HighSCORE ->" + str(h_scre), (250,150,0), 320,270)

    



        if 150 <= pos[0] <= 460 and 310 <= pos[1] <= 406:
            no_pg =1
            x_pg += 1

            if x_pg == 1:
                click_sound.play()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_sound.play()
                        game_over = False
                        if loop == "aam_zinagi":
                            aam_zinagi()

                        elif loop == 'mentos_zindagi':
                            mentos_zindagi()

                  
        

        
            

        else :
            no_pg = 0
            x_pg = 0


        if 509 <= pos[0] <= 579 and 335 <= pos[1] <= 359:
            no_e =1
            x_e += 1

            if x_e == 1:
                click_sound.play()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pygame.time.delay(100)
                        pygame.quit()
                        quit()

        else :
            no_e = 0
            x_e = 0


        #481 366 , 623 411


        if 481 < pos[0]< 623 and 366 < pos[1]< 411:
            no_m = 1
            x_m += 1

            if x_m == 1:
                click_sound.play()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_sound.play()
                        menu_scrn()

        else:
            no_m = 0
            x_m = 0



            
        pygame.display.update()
    pygame.quit()
    quit()


def gameover1v1(scre1, scre2):
    gm_ov_clr = (102,102,102)
    ball_img_png = pygame.image.load("Python/Games/reversed/images/ball.png")
    gmove_scr = pygame.image.load("Python/Games/reversed/images/Game_over_scrn.png")

    click_sound = mixer.Sound("Python/Games/reversed/audio/click.wav")
    ball_img = sprite_sheet.Spritesheet(ball_img_png)
    ball = ball_img.get_img(0,30,30,0.7,white) 
    
    no_pg = 0
    no_e = 0
    no_m = 0
    x_pg = 0
    x_e = 0
    x_m = 0

    
    end_game = False
    while not end_game:
        pos = pygame.mouse.get_pos()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
        play_ag = getimg("Python/Games/reversed/images/playag_script.png", no_pg,175, 60,1.7,black )
        exit = getimg("Python/Games/reversed/images/exit.png", no_e , 175,60,1,black)
        menu = getimg("Python/Games/reversed/images/menu_but.png", no_m,175,60,0.7,black)
        screen.fill(BG)
        blit_(screen,gmove_scr,0,0)
        blit_(screen,frame_0,lbat_x,lbat_y)
        blit_(screen,frame_1,rbat_x,rbat_y)    #509 335, 579 359
        blit_(screen,play_ag,160,320)
        blit_(screen,exit,460,320)
        blit_(screen,menu,490,370)
        font_render(font_p_,screen,"SCORE of Player1 ->" + str(scre1), (0,150,255), 245,235)
        font_render(font_p_, screen, "SCORE of Player2 ->" + str(scre2), (250,150,0), 245,270)

    



        if 150 <= pos[0] <= 460 and 310 <= pos[1] <= 406:
            no_pg =1
            x_pg += 1

            if x_pg == 1:
                click_sound.play()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_sound.play()
                        game_over = False
                        one_v_one()

        else:
            no_pg = 0
            x_pg = 0

        if 509 <= pos[0] <= 579 and 335 <= pos[1] <= 359:
            no_e =1
            x_e += 1

            if x_e == 1:
                click_sound.play()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pygame.time.delay(100)
                        pygame.quit()
                        quit()

        else :
            no_e = 0
            x_e = 0


        if 481 < pos[0]< 623 and 366 < pos[1]< 411:
            no_m = 1
            x_m += 1

            if x_m == 1:
                click_sound.play()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_sound.play()
                        menu_scrn()

        else:
            no_m = 0
            x_m = 0



        pygame.display.update()
    pygame.quit()
    quit()          

def credits_loop():
    pygame.init()
    end_game = False
    game_over = False

    BG = (0,0,0)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
  
    no_b = 0
    x_b = 0



    

    #sounds
    click_sound = mixer.Sound("Python/Games/reversed/audio/click.wav")


    clock = pygame.time.Clock()
    while not end_game:
        back_img = getimg("Python/Games/reversed/images/back_script.png", no_b,200,100,0.4,white)
        screen.fill(white)
        blit_(screen,back_img,5,0)

        pos = pygame.mouse.get_pos()


        if 0<=pos[0]<= 63 and 0<=pos[1]<= 34:
            no_b = 1
            x_b += 1

            if x_b == 1:
                click_sound.play()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_sound.play()
                        intro()
        else :
            no_b = 0
            x_b = 0
        font_render(font,screen,text01,black,0,50)
        font_render(font,screen,text_0, black,0,70)
        font_render(font,screen,text_1,black,0,90)
        font_render(font,screen,text_2,black,0,110)
        font_render(font,screen,text_3,black,0,130)
        font_render(font,screen,text_4,black,0,150)
        font_render(font,screen,text_5,black,0,170)
        font_render(font,screen,text_6,black,0,190)
        font_render(font,screen,text_7,black,0,210)
        font_render(font,screen,text_8,black,0,230)
        font_render(font,screen,text_9,black,0,250)
        font_render(font,screen,text_10,black,0,270)
        font_render(font,screen,text_11,black,0,290)
        font_render(font,screen,text_12,black,0,310)
        font_render(font,screen,text_13,black,0,330)
        font_render(font,screen,text_14,black,0,350)
        font_render(font,screen,text_15,black,0,370)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
        

        
        pygame.display.update()

    pygame.quit()
    quit()


def menu_scrn():
    end_game = False
    menu_scrn_img = pygame.image.load("Python/Games/reversed/images/menu_scr.png")
    no_ajb = 0
    no_mjb = 0
    no_1v1b = 0
    x = 0
    y = 0
    z = 0
    
    while not end_game:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
        pos = pygame.mouse.get_pos()
        aam_zinagi_imgscrp = getimg('Python/Games/reversed/images/aam_zindagi_butscrp.png',no_ajb,354,204,1,black)
        mentos_zindagi_imgscrp = getimg("Python/Games/reversed\images\mentos_zindagi_butscrp.png", no_mjb, 355,204,1,black)
        one_v_one_imgscrp = getimg("Python/Games/reversed/images/1v1_butscrp.png", no_1v1b,349, 204,1,black)

        click = mixer.Sound("Python/Games/reversed/audio/click.wav")


        blit_(screen,aam_zinagi_imgscrp,5,0)
        blit_(screen,mentos_zindagi_imgscrp,430,10)
        blit_(screen,one_v_one_imgscrp,210,280)


        if 0 < pos[0] <= 340 and 0< pos[1]<= 192:
            no_ajb = 1
            x += 1

            if x == 1:
                click.play()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        zhut('aam_zinagi')

        else:
            no_ajb = 0
            x = 0



        if 440 <= pos[0]<= 795 and 0 < pos[1] < 209:
            y += 1
            no_mjb = 1

            if y == 1 :
                click.play()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        zhut('mentos_zindagi')

        else:
            no_mjb = 0
            y= 0




        #228 267,553 472

        if 228 < pos[0] < 553 and 267<pos[1]<472:
            z += 1
            no_1v1b = 1

            if z == 1:
                click.play()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1:
                        one_v_one()

        else:
            no_1v1b = 0
            z = 0


        

            

                


        pygame.display.update()     
    pygame.quit()
    quit()

def zhut(loop):
    end_game = False
    clock = pygame.time.Clock()
    fps = 60
    zhut_y = 215
    

    while not end_game:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True

            elif event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    if loop == 'aam_zinagi':
                        aam_zinagi()

                    if loop == 'mentos_zindagi':
                        mentos_zindagi()
        zhut_img = getimg("Python/Games/reversed/images/zhut.png", 0,800,500,1,red)#215
        pts = getimg("Python/Games/reversed/images/ets.png", 0,334,96,1,white)
        screen.fill(BG)
        blit_(screen,zhut_img,0,0)
        screen.blit(pts, (screen.get_width()/2 - pts.get_width()/2, screen.get_height()/2 - pts.get_height()/2 + math.sin(time.time()*5)*5 )) 


        if zhut_y >= 215:
            zhut_y = zhut_y -2

        elif  zhut_y <= 95:
            zhut_y += 2


        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()
    quit()

def intro():







    pygame.init()
    end_game = False


    BG = (0,0,0)
    black = (0,0,0)
    white = (255,255,255)


        



    fps = 60

    no_p = 0
    no_c = 0
    x_c = 0
    x_p = 0

    # sounds
    click_sound = mixer.Sound("Python/Games/reversed/audio/click.wav")


    clock = pygame.time.Clock()


    while not end_game:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
        screen.fill(BG)
    

        intro_scr = getimg("Python/Games/reversed/images/intro.png",0,1410,744 , 0.5673758865248227,white)
        play = getimg("Python/Games/reversed/images/play_script.png", no_p,120,65,1,black)
        credits = getimg("Python/Games/reversed/images/credits_script.png",no_c , 148,64,1,black )

        

        blit_(screen,intro_scr,-15,40)
        blit_(screen,play,30,415)    #670
        blit_(screen,credits,325,415)
        if 29<= pos[0] <= 160 and  410<=pos[1]<= 500:
            no_p = 1
            x_p += 1

            if x_p == 1:
                click_sound.play()
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_sound.play()
                        menu_scrn()
        else :
            no_p = 0
            x_p = 0
        

        if 320<= pos[0]<= 475 and 420<= pos[1] <=464:
            no_c = 1
            x_c += 1
            if x_c == 1:
                click_sound.play()



            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click_sound.play()
                        credits_loop()
        else :
            no_c = 0
            x_c = 0


        clock.tick(fps)



        
        pygame.display.update()
    pygame.quit()
    quit()

intro()