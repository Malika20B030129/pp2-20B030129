import pygame 

pygame.init()

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0) 
width = 500
height = 500

screen = pygame.display.set_mode((width, height))

isPressed = False
prevPoint = (0, 0)
curPoint = (width//2,height//2)
er=(width,height)
def drawRectangle(surface, color, x, y, w, h):
    pygame.draw.rect(surface, color, [x, y, w, h], 5)

def drawCircle(surface, color, x, y):
    pygame.draw.circle(surface, color, (x, y), 30, 3)

def drawLine(surface, color, startPos, endPos):
    pygame.draw.line(surface, color, startPos, endPos, 2)

def erase(surface,color, x, y,w,h):
    pygame.draw.polygon(surface, color, [x,y,w,h])


currentTool = 0
toolCount = 6

current_color = 0
colors = (BLUE, GREEN, RED)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                currentTool = (currentTool + 1) % toolCount
            elif event.key == pygame.K_c:
                current_color = (current_color + 1) % len(colors)
            elif event.key== pygame.K_v:
                erase(screen, BLACK, (prevPoint[0],prevPoint[1]),(curPoint[0]+curPoint[0], prevPoint[1]),(curPoint[0]+curPoint[0], curPoint[1]+curPoint[1]), (prevPoint[0],curPoint[1]+curPoint[1]))
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPoint = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        if event.type == pygame.MOUSEMOTION and isPressed == True:
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
            
    if currentTool == 0:
        drawLine(screen, colors[current_color], prevPoint, curPoint)
    elif currentTool == 1:
        drawRectangle(screen, colors[current_color], curPoint[0], curPoint[1], 100, 100)
    elif currentTool == 2:
        drawCircle(screen, colors[current_color], *curPoint)
    elif currentTool== 3:
        pygame.draw.polygon(screen, colors[current_color], [(prevPoint[0], prevPoint[1]), (curPoint[0], curPoint[1]), (prevPoint[0], curPoint[1])],5)
    elif currentTool== 4:
        pygame.draw.polygon(screen, colors[current_color], [(curPoint[0], curPoint[1]), (curPoint[0]+curPoint[0], curPoint[1]),  (prevPoint[0] + (curPoint[0] - prevPoint[0])/2+curPoint[0], prevPoint[1])],5) 
    elif currentTool==5: 
        pygame.draw.polygon(screen, colors[current_color], [(curPoint[0], curPoint[1]), (curPoint[0]+curPoint[0]/2, (curPoint[1] + curPoint[1]/2) ), (curPoint[0], curPoint[1]+curPoint[1]), (curPoint[0]/2, (curPoint[1] +curPoint[1]/2))],5)
    
    pygame.display.flip()