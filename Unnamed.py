import os
import pygame
from pygame.locals import *


pygame.init()

FPS = 60
TRIG_FRAME = 5
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
anim = 0
pygame.display.set_caption('Space Fall')
Guide = False
wait_screen = True
wait_bg = pygame.image.load(f'assets/bg.png')
fr = [pygame.image.load(f'assets/keys/{i}.gif') for i in range(0, 23)]
wait_text1 = pygame.image.load(f'assets/text1.png')
wait_name1 = pygame.image.load(f'assets/name1.png')
wait_text1 = pygame.transform.scale(wait_text1, (500, 500))
wait_name1 = pygame.transform.scale(wait_name1, (500, 500))
wait_guide = pygame.image.load(f'assets/guide.png')
wait_guide = pygame.transform.scale(wait_guide, (300, 200))
wait_back = pygame.image.load(f'assets/back.png')
wait_bg1 = pygame.image.load(f'assets/bg1.png')
wait_back = pygame.transform.scale(wait_back, (300, 200))


def draw_wait_screen():
    global anim
    if anim + 1 >= 60:
        anim = 0
    screen.blit(wait_name1, (50, -150))
    screen.blit(wait_guide, (150, 500))
    anim += 1
    pygame.display.update()


def guide_screen():
    global  anim
    if anim + 1 >= 60:
        anim = 0
    screen.blit(wait_text1, (0, 25))
    screen.blit(pygame.transform.scale(fr[anim // 5].convert_alpha(), (300, 300)), (150, 350))
    screen.blit(wait_back, (-50, 665))
    anim += 1
    pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            wait_screen = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            wait_screen = True
            if 210 <= pygame.mouse.get_pos()[0] <= 400 and 580 <= pygame.mouse.get_pos()[1] <= 620:
                Guide = True
            if Guide == True and 5 <= pygame.mouse.get_pos()[0] <= 195 and 755 <= pygame.mouse.get_pos()[1] <= 795:
                Guide = False

    screen.fill(pygame.Color("black"))
    if wait_screen and Guide == False:
        screen.blit(wait_bg, (-1250, 0))
        draw_wait_screen()

    if Guide:
        screen.blit(wait_bg1, (0, 0))
        guide_screen()
    elif Guide == False and wait_screen == True:
        screen.blit(wait_bg, (-1250, 0))
        draw_wait_screen()
    else:
        screen.fill(pygame.Color("black"))
    print(pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
