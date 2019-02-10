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

# 载入飞机图片
plane_img = pygame.image.load(r'I:\pygadgets\aircraftwar\resources\image\shoot.png')
  
# 选择飞机在大图片中的位置，并生成subsurface，然后初始化飞机开始的位置
player_rect = pygame.Rect(0, 99, 102, 126)
player = plane_img.subsurface(player_rect)
player_pos = [200, 600]

while True:
    # 绘制背景
    screen.fill(0)
    screen.blit(background, (0, 0))

    # 绘制飞机
    screen.blit(player, player_pos)
    
    # 更新屏幕
    pygame.display.update()
    # 处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()