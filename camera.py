import pygame, sys
from random import randint

class Tree(pygame.sprite.Sprite):
    pass

class Player(pygame.sprite.Sprite):
    pass

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

camera_group = pygame.sprite.Group()
Player((640,360), camera_group)

for i in range(20):
    random_x = randint(0,1000)
    random_y = randint(0,1000)
    Tree((random_x,random_y),camera_group)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill('#71ddee')
    
    camera_group.update()
    camera_group.draw(screen)
    
    pygame.display.update()
    clock.tick(60)