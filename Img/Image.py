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
    return None
 
#photo.show()
#rotation_indirecte_sp(photo)
rotation_directe_sp(photo)
photo.show()
