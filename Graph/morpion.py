
import pygame
import time
import pygame.freetype
larg_case=200
surf=pygame.display.set_mode((3*larg_case+larg_case,3*larg_case))

couleur_ronds = (39,117,238)
couleur_croix = (237,28,28)
run=True
pygame.draw.line(surf,(255,255,255),(larg_case,0),(larg_case,3*larg_case),4)
pygame.draw.line(surf,(255,255,255),(2*larg_case,0),(2*larg_case,3*larg_case),4)
pygame.draw.line(surf,(255,255,255),(0,larg_case),(3*larg_case,larg_case),4)
pygame.draw.line(surf,(255,255,255),(0,2*larg_case),(3*larg_case,2*larg_case),4)
joueur=1
tab=[[0 for j in range(3)] for i in range(3)]
pygame.init()

pygame.font.init()
font = pygame.font.SysFont('Arial', 20)
bt1 = pygame.Rect(larg_case*3+10, larg_case//3, larg_case -20 , larg_case//2)
bt2 = pygame.Rect(larg_case*3+10, larg_case+larg_case//3, larg_case -20, larg_case//2)
bt3 = pygame.Rect(larg_case*3+10, larg_case*2+larg_case//3, larg_case-20, larg_case//2)

pass
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
    
    #Cas nul 
    count = 0
    for i in range(3):
        for j in range(3) :
            if tab[i][j] != 0 :
                count += 1
    if count == 9 :
        return (True, 3)


    return (False,0) 

def interface(surf, pos,i) :
    pygame.draw.rect(surf, (255,255,255),bt1,5)
    pygame.draw.rect(surf,(255,255,255), bt2,5)
    pygame.draw.rect(surf,(255,255,255), bt3,5)
    
    tab_test = ["Joueur 1", "Facile", "Medium", "Impossible"]
    
    if bt1.collidepoint(pos) :
        i+=1
    bt1_surf = font.render(tab_test[i], True, (255,255,255))
    
    bt2_surf = font.render("Joueur 2", True, (255,255,255))
    bt3_surf = font.render("Commencer", True,(255,255,255))
    
    coordonne = bt1.midleft
    larg , haut = bt1_surf.get_size()
    surf.blit(bt1_surf,(coordonne[0]+ larg//2, coordonne[1]- haut//2))

    coordonne = bt2.midleft
    larg , haut = bt2_surf.get_size()
    surf.blit(bt2_surf,(coordonne[0]+ larg//2, coordonne[1]- haut//2))

    coordonne = bt3.midleft
    larg , haut = bt3_surf.get_size()
    surf.blit(bt3_surf,(coordonne[0]+ larg//3, coordonne[1]- haut//2))

    surf.blit(surf,(0,0))
i = 0
interface(surf,pygame.mouse.get_pos(),i)
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        
        
        
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
                interface(surf,pygame.mouse.get_pos(),i)
                pos=pygame.mouse.get_pos()
                case=(pos[0]//larg_case,pos[1]//larg_case)
                #print(case)
                
                
                if case[0] < 3 : # Si est dans la grille de jeu
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
                        elif val_verif[1] == 2 :
                            couleur = couleur_croix
                        else :
                            couleur = (255,255,255)

                        
                        if val_verif[1] == 3 :
                            text_surface = font.render(f"Partie nul ! whaouuuu (c'est pas fou fou)", False, couleur)
                            text_x,text_y = text_surface.get_size()    
                        else :
                            text_surface = font.render(f"le joueur {val_verif[1]} a gagné ! whaouuuu trop fort bg tu gères", False, couleur)
                            text_x,text_y = text_surface.get_size()
                        
                        surf.blit(text_surface, (((larg_case*3)//2)-text_x//2,((larg_case*3)//2)-text_y//2))
                        pygame.display.flip()
                        time.sleep(3)
                        run = False
                    
    pygame.display.flip()          
pygame.quit()

