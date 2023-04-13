import pygame
larg_case=200
surf=pygame.display.set_mode((3*larg_case,3*larg_case))

run=True
pygame.draw.line(surf,(255,255,255),(larg_case,0),(larg_case,3*larg_case),4)
pygame.draw.line(surf,(255,255,255),(2*larg_case,0),(2*larg_case,3*larg_case),4)
pygame.draw.line(surf,(255,255,255),(0,larg_case),(3*larg_case,larg_case),4)
pygame.draw.line(surf,(255,255,255),(0,2*larg_case),(3*larg_case,2*larg_case),4)
joueur=1
tab=[[False for j in range(3)] for i in range(3)]

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1,0,0) :
                pos=pygame.mouse.get_pos()
                case=(pos[0]//larg_case,pos[1]//larg_case)
                print(case)
                if tab[case[1]][case[0]]==False:
                    tab[case[1]][case[0]]=True
                    if joueur==1:
                        pygame.draw.circle(surf,(121,173,242),(case[0]*larg_case+larg_case//2,case[1]*larg_case+larg_case//2),(int(0.475*larg_case)),4)
                        joueur=2
                    else:
                        pygame.draw.line(surf,(238,51,76),(int(case[0]*larg_case+0.05*larg_case),int(case[1]*larg_case+0.05*larg_case)),(int(case[0]*larg_case+0.95*larg_case),int(case[1]*larg_case+0.95*larg_case)),4)
                        pygame.draw.line(surf,(238,51,76),(int(case[0]*larg_case+0.95*larg_case),int(case[1]*larg_case+0.05*larg_case)),(int(case[0]*larg_case+0.05*larg_case),int(case[1]*larg_case+0.95*larg_case)),4)
                        joueur=1
                    
    pygame.display.flip()          
pygame.quit()
