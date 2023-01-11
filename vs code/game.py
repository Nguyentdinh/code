import pygame
from random import randrange

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0,0,0)
WHILE = (255,255,255)
BLUE =  (0,0,255)
clock = pygame.time.Clock()
# rect_x = 100
# rect_y = 200
font = pygame.font.SysFont('sans',30)
text = font.render("random", True, BLACK)
text_box = text.get_rect()

random_pos = (50,50)

circle_color = RED
while running :
    clock.tick(60)
    screen.fill(WHILE)

    # rect_x += 1
    # rect_y += 1
    mouse_x, mouse_y = pygame.mouse.get_pos()

    pygame.draw.rect(screen,WHILE,(random_pos[0],random_pos[1],text_box[2],text_box[3]))
    pygame.draw.circle(screen,circle_color,(200,370),30)
    screen.blit(text,random_pos)

    if ((mouse_x>random_pos[0]) and (mouse_x<random_pos[0]+text_box[2]) and (mouse_y>random_pos[1]) and (mouse_y<random_pos[1]+text_box[3])):
        text = font.render("random", True, BLUE)
        pygame.draw.line(screen,BLUE,(random_pos[0],random_pos[1]+text_box[3]+3),(random_pos[0]+text_box[2],random_pos[1]+text_box[3]+3))
    else:
        text = font.render("random", True, BLACK)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if ((mouse_x>random_pos[0]) and (mouse_x<random_pos[0]+text_box[2]) and (mouse_y>random_pos[1]) and (mouse_y<random_pos[1]+text_box[3])):
                    circle_color = ((randrange(0,255)),(randrange(0,255)),(randrange(0,255)))
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()

pygame.quit()
