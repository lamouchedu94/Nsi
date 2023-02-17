from PIL import Image

import time 

def rotation_indirecte(img):
    hauteur,largeur=img.size
    tourne=Image.new(mode='RGB',size=(hauteur,largeur))
    for ligne in range(hauteur):
        for colonne in range(largeur):
            tourne.putpixel((ligne,colonne),img.getpixel((colonne,largeur-1-ligne)))
    return tourne

def rotation_directe(img):
    hauteur,largeur=img.size
    tourne=Image.new(mode='RGB',size=(hauteur,largeur))
    for ligne in range(hauteur):
        for colonne in range(largeur):
            tourne.putpixel((ligne,colonne),img.getpixel((largeur-1-colonne,ligne)))
    return tourne

def rotation_indirecte_sp(img):
    hauteur,largeur=img.size
    for ligne in range(hauteur//2):
        for colonne in range(largeur//2):
            temp=img.getpixel((ligne,colonne))
            img.putpixel((ligne,colonne),img.getpixel((colonne,largeur-1-ligne)))
            img.putpixel((colonne,largeur-1-ligne),img.getpixel((largeur-1-ligne,largeur-1-colonne)))
            img.putpixel((largeur-1-ligne,largeur-1-colonne),img.getpixel((largeur-1-colonne,ligne)))
            img.putpixel((largeur-1-colonne,ligne),temp)
    return None

def rotation_directe_sp(img):
    hauteur,largeur=img.size
    for ligne in range(hauteur//2):
        for colonne in range(largeur//2):
            temp=img.getpixel((ligne,colonne))
            img.putpixel((ligne,colonne),img.getpixel((largeur-1-colonne,ligne)))
            img.putpixel((largeur-1-colonne,ligne),img.getpixel((largeur-1-ligne,largeur-1-colonne)))
            img.putpixel((largeur-1-ligne,largeur-1-colonne),img.getpixel((colonne,largeur-1-ligne)))
            img.putpixel((colonne,largeur-1-ligne),temp)
    return None

def rotation_directe_recu(img):
    h=img.size[0]//2
    if h>=1:
        a=rotation_directe_recu(img.crop((0,0,h,h)))
        b=rotation_directe_recu(img.crop((0,h,h,2*h)))
        c=rotation_directe_recu(img.crop((h,0,2*h,h)))
        d=rotation_directe_recu(img.crop((h,h,2*h,2*h)))
        img.paste(a,(h,0))
        img.paste(b,(0,0))
        img.paste(c,(h,h))
        img.paste(d,(0,h))
    return img

def rotation_indirecte_recu_sp(img,h=0,g=0,taille=None):
    if taille==None:
        taille=img.size[0]
    if taille>=1:
        k=taille//2
        rotation_indirecte_recu_sp(img,h,g,k)
        rotation_indirecte_recu_sp(img,h,g+k,k)
        rotation_indirecte_recu_sp(img,h+k,g,k)
        rotation_indirecte_recu_sp(img,h+k,g+k,k)
        permutation_indirecte(img,h,g,taille)
    return None

def permutation_indirecte(img,h,g,taille):
    k=taille//2
    temp=img.crop((h,g,h+k,g+k))
    img.paste(img.crop((h,g+k,h+k,g+2*k)),(h,g))
    img.paste(img.crop((h+k,g+k,h+2*k,g+2*k)),(h,g+k))
    img.paste(img.crop((h+k,g,h+2*k,g+k)),(h+k,g+k))
    img.paste(temp,(h+k,g))
    return None
    
#def permutation_indirecte_px(img,h,g,taille):
    
def ajout_carre(img):
    h,l=img.size
    dim=l
    if h>l:
        dim=h
    cpt=0
    while 2**cpt<dim:
        cpt+=1
    fond=Image.new('RGB',(2**cpt,2**cpt),'red')
    fond.paste(img,(0,0))
    return fond

def rotation_indirecte_gen(img):
    l,h=img.size
    if h!=l or h & (h-1)!=0:
        img=ajout_carre(img)
    dim=img.size[0]
    rotation_indirecte_sp(img)
    return img.crop((dim-h, 0, dim,l))

photo=Image.open('Img/chien2.jpg')
photo=rotation_indirecte_gen(photo)
photo.show()

"""
def f():
    for i in range(100):
        #rotation_directe_sp(photo)
        rota_recurs(photo)
    
    
    #time.sleep(10)

f()
"""
"""
print(process.memory_info().rss)
mem_usage = memory_usage(f)
print('Memory usage (in chunks of .1 seconds): %s' % mem_usage)
print('Maximum memory usage: %s' % max(mem_usage))
"""
