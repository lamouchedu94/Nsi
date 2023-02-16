from PIL import Image
'''
a = Image.open("Img/photo.bmp")
#a.show()

hauteur, largeur = a.size
tourne= Image.new(mode='RGB', size=(hauteur, largeur))

for ligne in range(hauteur) :
    for colone in range(largeur) :
        tourne.putpixel((ligne,colone), a.getpixel((hauteur-1-colone, ligne)))
tourne.show()

def anti_horaire(nom) :
    photo = Image.open(nom)
    hauteur, largeur = photo.size
    tourne= Image.new(mode='RGB', size=(hauteur, largeur))

    for ligne in range(hauteur) :
        for colone in range(largeur) :
            tourne.putpixel((ligne,colone), photo.getpixel((hauteur-1-colone, ligne)))
    return tourne

def horaire(nom) :
    photo = Image.open(nom)
    hauteur, largeur = photo.size
    tourne= Image.new(mode='RGB', size=(hauteur, largeur))

    for ligne in range(hauteur) :
        for colone in range(largeur) :
            tourne.putpixel((ligne,colone), photo.getpixel((colone, largeur-1-ligne)))
    return tourne


def anti_horaire_sp(nom) :
    photo = Image.open(nom)
    hauteur, largeur = photo.size

    for ligne in range(hauteur) :
        for colone in range(largeur) :
            photo.putpixel((ligne,colone), photo.getpixel((hauteur-1-colone, ligne)))
    photo.show()
    return None

def horaire_sp(nom) :
    photo = Image.open(nom)
    hauteur, largeur = photo.size
    for ligne in range(hauteur//2) :
        for colone in range(largeur//2) :
            temp = []
            temp.append(photo.getpixel(((ligne,colone))))
            temp.append(photo.getpixel((colone, largeur-1-ligne)))
            temp.append(photo.getpixel((hauteur- 1- colone,largeur-1-ligne)))
            temp.append(photo.getpixel((colone,largeur-1-ligne)))
            
            photo.putpixel((hauteur- 1- colone,ligne), temp[0])    
            photo.putpixel((colone, largeur-1-ligne), temp[2])
            photo.putpixel((hauteur- 1- colone,largeur-1-ligne),temp[3])
            photo.putpixel((ligne,colone), temp[2])
            
    photo.show()
    return None

horaire_sp("Img/photo.bmp")

def gen_photo(long, larg) :
    res = []
    count = 0
    for _ in range(larg):
        temp = []
        for _ in range(long):
            count += 1
            temp.append(count)
        res.append(temp)
    return res

def affichage(tab):
    if tab == None :
        return
    for ligne in tab :
        print(ligne)

photo = gen_photo(3,4)
affichage(photo)

def rotation(photo):
    colone = len(photo[0])
    res = []
    for i in range(colone):
        n_ligne = []
        for j in range(len(photo) - 1, -1, -1):
            ligne = photo[j]
            n_ligne.append(ligne[i])
        res.append(n_ligne)
    return res

new = rotation(photo)
print()
affichage(new)
'''
from PIL import Image
photo=Image.open('Img/photo.bmp')
import time 


def rotation_indirecte(img):
    hauteur,largeur=photo.size
    tourne=Image.new(mode='RGB',size=(hauteur,largeur))
    for ligne in range(hauteur):
        for colonne in range(largeur):
            tourne.putpixel((ligne,colonne),photo.getpixel((colonne,largeur-1-ligne)))
    return tourne
 
def rotation_directe(img):
    hauteur,largeur=photo.size
    tourne=Image.new(mode='RGB',size=(hauteur,largeur))
    for ligne in range(hauteur):
        for colonne in range(largeur):
            tourne.putpixel((ligne,colonne),photo.getpixel((largeur-1-colonne,ligne)))
    return tourne
 
def rotation_indirecte_sp(img):
    hauteur,largeur=img.size
    for ligne in range(hauteur//2):
        for colonne in range(largeur//2):
            temp=img.getpixel((ligne,colonne))
            photo.putpixel((ligne,colonne),photo.getpixel((colonne,largeur-1-ligne)))
            photo.putpixel((colonne,largeur-1-ligne),photo.getpixel((largeur-1-ligne,largeur-1-colonne)))
            photo.putpixel((largeur-1-ligne,largeur-1-colonne),photo.getpixel((largeur-1-colonne,ligne)))
            photo.putpixel((largeur-1-colonne,ligne),temp)
    return None
 
def rotation_directe_sp(img):
    hauteur,largeur=img.size
    for ligne in range(hauteur//2):
        for colonne in range(largeur//2):
            temp=img.getpixel((ligne,colonne))
            
            photo.putpixel((ligne,colonne),photo.getpixel((largeur-1-colonne,ligne)))
            photo.putpixel((largeur-1-colonne,ligne),photo.getpixel((hauteur-1-ligne, largeur-1-colonne)))
            photo.putpixel((hauteur-1-ligne, largeur-1-colonne),photo.getpixel((colonne,hauteur-1-ligne)))
            photo.putpixel((colonne,hauteur-1-ligne),temp)
    
    #img.show()
    return None
 
#photo.show()
#rotation_indirecte_sp(photo)
#rotation_directe_sp(photo)
#photo.show()

def rota_recurs(img):
    h = img.size[0]//2
    if h>=1:
        a = rota_recurs(img.crop((0, 0, h, h)))
        b = rota_recurs(img.crop((0, h, h, 2*h)))
        c = rota_recurs(img.crop((h,0,2*h,h)))
        d = rota_recurs(img.crop((h,h,2*h,2*h)))
        img.paste(a,(h, 0))
        img.paste(b,(0,0))
        img.paste(c,(h,h))
        img.paste(d,(0,h))
    return img
    
def rotation_dire_recu_sp(img, h=0,g=0, taille= None):
    if taille==None :
        taille=img.size[0]
    if taille>= 1 :
        k=taille//2
        rotation_dire_recu_sp(img,h,g,k)
        rotation_dire_recu_sp(img,h,g+k,k)
        rotation_dire_recu_sp(img,h+k,g,k)
        rotation_dire_recu_sp(img,h+k,g+k,k)
        permutation_indirecte(img,h,g,taille)
    return None
#rota_recurs(photo).show()

def permutation_indirecte(img,h,g,taille):
    k = taille//2
    temp = img.crop((h,g,k+h,g+k))
    img.paste(img.crop((h,g+k,h+k, g+2*k)), (h,g))
    img.paste(img.crop((h,g+k,h+2*k, g+2*k)), (h,g+k))
    img.paste(img.crop((h+k,g+k,h+2*k, g+2*k)), (h,g+k))
    img.paste(temp, (h+k,g))
    return None
    
def permutation_directe(img,h,g,taille):
    pass

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
