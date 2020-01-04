import os
import pygame
from pygame.locals import *


pygame.init()
pygame.mixer.init()

n = -800
n1 = -1600
FPS = 60
TRIG_FRAME = 5
WIDTH = 600
HEIGHT = 800
x, y = 225, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
anim = 0
pygame.display.set_caption('Space Fall')
Hard = True
Options = False
Guide = False
wait_screen = True
Prepair = False
game = False
RIGHT = False
DOWN = False
UP = False
LEFT = False
seconds = 0
shipN = 0
x1 = 0
y1 = 0
lvl1_bg = pygame.image.load(f'assets/game1.jpg')
lvl1_bg1 = pygame.image.load(f'assets/game1.jpg')
wait_bg = pygame.image.load(f'assets/bg.png')
fr = [pygame.image.load(f'assets/keys/{i}.gif') for i in range(0, 23)]
ships = [pygame.image.load(f'assets/ships/ship ({i}).png').convert_alpha() for i in range(1, 16)]
wait_text1 = pygame.image.load(f'assets/text1.png')
wait_name1 = pygame.image.load(f'assets/name1.png')
wait_text1 = pygame.transform.scale(wait_text1, (500, 500))
wait_name1 = pygame.transform.scale(wait_name1, (500, 500))

wait_guide = pygame.image.load(f'assets/guide.png')
wait_guide = pygame.transform.scale(wait_guide, (300, 200))

wait_bg1 = pygame.image.load(f'assets/bg1.png')

wait_back = pygame.image.load(f'assets/back.png')
wait_back = pygame.transform.scale(wait_back, (300, 200))

wait_back1 = pygame.image.load(f'assets/back1.png')
wait_back1 = pygame.transform.scale(wait_back1, (300, 200))

wait_guide1 = pygame.image.load(f'assets/guide1.png')
wait_guide1 = pygame.transform.scale(wait_guide1, (300, 200))

wait_play = pygame.image.load(f'assets/play.png')
wait_play = pygame.transform.scale(wait_play, (300, 200))

wait_play1 = pygame.image.load(f'assets/play1.png')
wait_play1 = pygame.transform.scale(wait_play1, (300, 200))

wait_cont1 = pygame.image.load(f'assets/cont1.png')
wait_cont1 = pygame.transform.scale(wait_cont1, (300, 200))

wait_cont = pygame.image.load(f'assets/cont.png')
wait_cont = pygame.transform.scale(wait_cont, (300, 200))

wait_opt1 = pygame.image.load(f'assets/options1.png')
wait_opt1 = pygame.transform.scale(wait_opt1, (300, 200))

opt_music = pygame.image.load(f'assets/MT.png')

opt_music1 = pygame.image.load(f'assets/MF.png')

arrow1 = pygame.image.load(f'assets/arrow1.png')
arrow2 = pygame.image.load(f'assets/arrow2.png')

wait_opt = pygame.image.load(f'assets/options.png')
wait_opt = pygame.transform.scale(wait_opt, (300, 200))
pygame.mixer.music.load('assets/sounds/bg.mp3')

with open('assets/st.txt', 'r', encoding='utf-8') as f:
    i = f.read()
    i = i.split(';')
    if i[0] == '0':
        Hard = False
    else:
        Hard = True
    if i[2] == '1':
        sound = '1'
        pygame.mixer.music.play(-1)
    else:
        sound = '0'

def draw_wait_screen():
    screen.blit(wait_name1, (50, -150))
    if Hard == False:
        if Guide == False and wait_screen == True and \
                210 <= pygame.mouse.get_pos()[0] <= 400 and 430 <= pygame.mouse.get_pos()[1] <= 470:
            screen.blit(wait_cont1, (150, 350))
        else:
            screen.blit(wait_cont, (150, 350))
    if Guide == False and wait_screen == True and \
                    210 <= pygame.mouse.get_pos()[0] <= 400 and 530 <= pygame.mouse.get_pos()[1] <= 570:
        screen.blit(wait_opt1, (150, 450))
    else:
        screen.blit(wait_opt, (150, 450))
    if Guide == False and wait_screen == True and \
                    210 <= pygame.mouse.get_pos()[0] <= 400 and 480 <= pygame.mouse.get_pos()[1] <= 520:
        screen.blit(wait_play1, (150, 400))
    else:
        screen.blit(wait_play, (150, 400))
    if Guide == False and wait_screen == True and \
                    210 <= pygame.mouse.get_pos()[0] <= 400 and 580 <= pygame.mouse.get_pos()[1] <= 620:
        screen.blit(wait_guide1, (150, 500))
    else:
        screen.blit(wait_guide, (150, 500))

    pygame.display.update()


def guide_screen():
    global anim
    if anim + 1 >= FPS:
        anim = 0
    screen.blit(wait_text1, (0, 25))
    screen.blit(pygame.transform.scale(fr[anim // 5].convert_alpha(), (300, 300)), (150, 350))
    if Guide == True and 15 <= pygame.mouse.get_pos()[0] <= 200 and 745 <= pygame.mouse.get_pos()[1] <= 785:
        screen.blit(wait_back1, (-50, 665))
    else:
        screen.blit(wait_back, (-50, 665))
    anim += 1
    pygame.display.update()

def options_screen():
    if Options == True and 15 <= pygame.mouse.get_pos()[0] <= 200 and 745 <= pygame.mouse.get_pos()[1] <= 785:
        screen.blit(wait_back1, (-50, 665))
    else:
        screen.blit(wait_back, (-50, 665))
    if sound == '1':
        screen.blit(pygame.transform.scale(opt_music, (600, 150)), (50, 150))
    else:
        screen.blit(pygame.transform.scale(opt_music1, (600, 150)) , (50, 150))
    pygame.display.update()

def prepair_screen():
    global  shipN
    global anim
    if anim + 1 >= FPS:
        anim = 0
    if Prepair == True and 15 <= pygame.mouse.get_pos()[0] <= 200 and 745 <= pygame.mouse.get_pos()[1] <= 785:
        screen.blit(wait_back1, (-50, 665))
    else:
        screen.blit(wait_back, (-50, 665))


    screen.blit(pygame.transform.scale(arrow1, (45, 50)), (380, 393))
    screen.blit(pygame.transform.scale(arrow2, (45, 50)), (170, 400))
    screen.blit(pygame.transform.scale(ships[shipN], (150, 150)), (225, 350))
    pygame.display.update()

def game_lvl1():
    screen.blit(pygame.transform.scale(ships[shipN], (105, 105)), (x, y))
    pygame.display.update()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                LEFT = True
                x1 = 8
            if event.key == pygame.K_RIGHT:
                RIGHT = True
                x1 = 8
            if event.key == pygame.K_DOWN:
                DOWN = True
                y1 = 8
            if event.key == pygame.K_UP:
                UP = True
                y1 = 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                RIGHT, LEFT = False, False
                x1 = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                UP, DOWN = False, False
                y1 = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Guide == False and Options == False and wait_screen == True and Prepair == False and \
                    210 <= pygame.mouse.get_pos()[0] <= 400 and 580 <= pygame.mouse.get_pos()[1] <= 620:
                Guide = True
                wait_screen = False
                anim = 0

            if Guide == True and 5 <= pygame.mouse.get_pos()[0] <= 195 and 755 <= pygame.mouse.get_pos()[1] <= 795:
                Guide = False
                wait_screen = True
            if Options == False and wait_screen == True and Guide == False and \
                    210 <= pygame.mouse.get_pos()[0] <= 400 and 530 <= pygame.mouse.get_pos()[1] <= 570:
                Options = True
                wait_screen = False

            if Options == True and 15 <= pygame.mouse.get_pos()[0] <= 200 and 745 <= pygame.mouse.get_pos()[1] <= 785:
                Options = False
                wait_screen = True
            if Options == True and 115 <= pygame.mouse.get_pos()[0] <= 530 and 210 <= pygame.mouse.get_pos()[1] <= 255:
                if sound == '1':
                    sound = '0'
                else:
                    sound = '1'
                if sound == '1':
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
                with open('assets/st.txt', 'w', encoding='utf-8') as f:
                    f.write(f'0;0;{sound};')
            if Guide == False and wait_screen == True and Options == False and \
                    210 <= pygame.mouse.get_pos()[0] <= 400 and 480 <= pygame.mouse.get_pos()[1] <= 520:
                seconds = 0
                screen.fill(pygame.Color("black"))
                wait_screen = False
                Prepair = True

            if Prepair == True and Guide == False and Options == False and wait_screen == False and \
                    15 <= pygame.mouse.get_pos()[0] <= 200 and 745 <= pygame.mouse.get_pos()[1] <= 785:
                Prepair = False
                wait_screen = True

            if Prepair == True and Guide == False and Options == False and wait_screen == False and \
                    170 <= pygame.mouse.get_pos()[0] <= 210 and 405 <= pygame.mouse.get_pos()[1] <= 440:
                if shipN == 0:
                    pass
                else:
                    shipN -= 1
                print(shipN)

            if Prepair == True and Guide == False and Options == False and wait_screen == False and \
                    380 <= pygame.mouse.get_pos()[0] <= 425 and 400 <= pygame.mouse.get_pos()[1] <= 435:
                if shipN == 14:
                    pass
                else:
                    shipN += 1
                print(shipN)
                game = True
                Prepair = False



    screen.fill(pygame.Color("black"))
    if wait_screen and Guide == False and Options == False and Prepair == False and game == False:
        screen.blit(wait_bg, (-1250, 0))
        draw_wait_screen()
    if Guide:
        screen.blit(wait_bg1, (0, 0))
        guide_screen()
    elif Options:
        screen.blit(wait_bg1, (0, 0))
        options_screen()
    elif Prepair:
        screen.blit(wait_bg1, (0, 0))
        prepair_screen()
    elif game:
        screen.fill((0, 0, 0))
        if LEFT:
            if x <= 1:
                pass
            else:
                x -= x1
        if RIGHT:
            if x >= 490:
                pass
            else:
                x += x1
        if UP:
            if y <= 450:
                pass
            else:
                y -= y1
        if DOWN:
            if y >= 690:
                pass
            else:
                y += y1
        game_lvl1()

    print(pygame.mouse.get_pos(), int(clock.get_fps()), game, Prepair, x, y)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
