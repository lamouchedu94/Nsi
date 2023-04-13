import pygame
import time
larg_case=200
surf=pygame.display.set_mode((3*larg_case,3*larg_case))

couleur_ronds = (39,117,238)
couleur_croix = (237,28,28)
run=True
pygame.draw.line(surf,(255,255,255),(larg_case,0),(larg_case,3*larg_case),4)
pygame.draw.line(surf,(255,255,255),(2*larg_case,0),(2*larg_case,3*larg_case),4)
pygame.draw.line(surf,(255,255,255),(0,larg_case),(3*larg_case,larg_case),4)
pygame.draw.line(surf,(255,255,255),(0,2*larg_case),(3*larg_case,2*larg_case),4)
joueur=1
tab=[[0 for j in range(3)] for i in range(3)]

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

def verif(tab) :
    #cas vertical
    count = 0
    for i in range(3):
        for ligne in tab :
            if ligne[i] == 1 :
                count += 1
        if count == 3 :
            return (True,1)
        count = 0
    for i in range(3):
        for ligne in tab :
            if ligne[i] == 2 :
                count += 1
        if count == 3 :
            return (True,2)
        count = 0

    #cas horizontal
    count = 0 
    for i in range(3):
        for j in range(3) :
            if tab[i][j] == 1 :
                count += 1
        if count == 3 :
            return (True, 1)
        count = 0 
    
    count = 0
    for i in range(3):
        for j in range(3) :
            if tab[i][j] == 2 :
                count += 1 
        if count == 3 :
            return (True, 2)
        count = 0
    
    #cas diagonales 
    #polo est un petit caca    

    count = 0
    for i in range(3) :
        if tab[i][i] == 1 :
            count += 1 
    if count == 3 :
        return (True, 1)
    
    count = 0
    for i in range(3) :
        if tab[i][i] == 2 :
            count += 1 
    if count == 3 :
        return (True, 2)

    count = 0
    ind = 0 
    for i in range(2,-1,-1) :
        if tab[i][ind] == 1 :
            count += 1
        ind += 1 
    if count == 3 :
        return (True, 1)

    count = 0
    ind = 0 
    for i in range(2,-1,-1) :
        if tab[i][ind] == 2 :
            count += 1
        ind += 1 
    if count == 3 :
        return (True, 2)
    
    return (False,0) 

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
                pos=pygame.mouse.get_pos()
                case=(pos[0]//larg_case,pos[1]//larg_case)
                #print(case)
                
                if tab[case[1]][case[0]]==0:
                    if joueur==1:
                        pygame.draw.circle(surf,couleur_ronds,(case[0]*larg_case+larg_case//2,case[1]*larg_case+larg_case//2),(int(0.475*larg_case)),4)
                        tab[case[1]][case[0]] = 1
                        joueur=2
                    else:
                        pygame.draw.line(surf,couleur_croix,(int(case[0]*larg_case+0.05*larg_case),int(case[1]*larg_case+0.05*larg_case)),(int(case[0]*larg_case+0.95*larg_case),int(case[1]*larg_case+0.95*larg_case)),4)
                        pygame.draw.line(surf,couleur_croix,(int(case[0]*larg_case+0.95*larg_case),int(case[1]*larg_case+0.05*larg_case)),(int(case[0]*larg_case+0.05*larg_case),int(case[1]*larg_case+0.95*larg_case)),4)
                        tab[case[1]][case[0]] = 2
                        joueur=1
            val_verif = verif(tab)
            if val_verif[0] == True:
                surf.fill((0,0,0))
                
                if val_verif[1] == 1 :
                    couleur = couleur_ronds
                else :
                    couleur = couleur_croix
                
                text_surface = font.render(f"le joueur {val_verif[1]} a gagné ! whaouuuu trop fort bg tu gères", False, couleur)
                text_x,text_y = text_surface.get_size()
                surf.blit(text_surface, (((larg_case*3)//2)-text_x//2,((larg_case*3)//2)-text_y//2))
                pygame.display.flip()
                time.sleep(3)
                run = False
                    
    pygame.display.flip()          
pygame.quit()
