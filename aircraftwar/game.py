# -*- coding: utf-8 -*-

import pygame
import pygame
from pygame.locals import *
from sys import exit

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

# 初始化游戏
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('飞机大战')

# 载入背景图
background = pygame.image.load(r'I:\pygadgets\aircraftwar\resources\image\background.png')

print(background)

while True:
    # 绘制背景
    screen.fill(0)
    screen.blit(background, (0, 0))
    # 更新屏幕
    pygame.display.update()
    # 处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()