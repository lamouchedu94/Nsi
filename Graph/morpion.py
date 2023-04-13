import pygame


run = True
larg_case = 200
haut_case = 200
surf = pygame.display.set_mode((800,800))
while run :
    pygame.draw.line(surf, (0,255,255), (0,0),(200, 200),10)
    pygame.draw.line(surf,(255,255,255),(10,20),(150,200),2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.mouse.get_pressed() == (1,0,0) :
                pos = pygame.mouse.get_pos()
                print(pos)
    

    pygame.draw.line(surf, (0,255,255), (200,0),(200, haut_case*3),10)


    surf.fill((0,0,0))
    pygame.display.flip()
pygame.quit()
