import pygame
pygame.init()
width  = 490
length = 490
screen = pygame.display.set_mode((width, length))
done = False

x = width/2
y = length/2
radius = 25
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]    and y>=30:  y-=20
    if pressed[pygame.K_DOWN]  and y<=width-30: y+=20
    if pressed[pygame.K_LEFT]  and x>=30:  x-=20
    if pressed[pygame.K_RIGHT] and x<length-30: x+=20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    pygame.display.flip()
clock.tick(30)