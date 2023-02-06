
	

'''
Changement de base
Auteurs : FOUILLOUX Jérémy, GRILIKHES Garance, CASSAN Paul, GODIN Paul
Date : 07/02/22
L'utilisateur rentre une base de départ, un nombre écrit dans cette base et la base dans laquelle il faut convertir le nombre.
'''

def converts(nb):
    '''
    Cette fonction prend en argument 1 parametre nombre qui est une chaine de caractère contenant des shadocks. Elle convertit les shadocks en base 4 et renvoie le résultat sous forme de chaine de caractère.
    '''
    rep=""
    for i in nb :
        if i == 'G' :
            rep +='0'
        elif i == 'B' :
            rep +='1'
        elif i == 'Z' :
            rep +='2'
        elif i == 'M' :
            rep +='3'         
    return rep

assert converts("BUGAZO")=="102"
assert converts("ZOBUGAGA") == "2100"
assert converts("BU") == "1"

def convertir_Base_n(nb,base): 
    '''Cette Fonction prend en argument 2 parametres : nombre est un entier en base 10 et base qui est une chaine. Cette fonction renvoie le nombre convertis dans la base demandée sous frome de chaine.'''
    base = int(base)
    lettres = 'ABCDEF'
    valeur = 0
    rep = ""
    while nb >= 1 :
        valeur = nb%base
        if valeur > 9 :
            rep = lettres[valeur-10] + rep 
        else :
            rep = str(valeur) +rep
        nb = nb//base
    return rep
assert convertir_Base_n(79,16)=='4F'
assert convertir_Base_n(79, 6)=="211"

def convertion_Base10(nb,basedepart):
    '''Cette fonction prend en argument 2 parametres nb est une chaine de caractere et basedepart un entier. Elle renvoie le nombre converti en base 10 sous forme d'entier'''
    basedepart=int(basedepart)
    rep = 0
    lettres = 'ABCDEF'
    for i in range(len(nb)) :   
        if nb[i] in lettres :   #Teste la présence ou non d'une lettre
            for a in range(len(lettres)) :
                car = lettres[a]    
                if nb[i] == car :   #Compare une lettre (variable car) avec les lettres de la variable "lettres"
                    rep+= (10+a)*basedepart**(len(nb)-i-1)
        else :
            rep+= int(nb[i])*basedepart**(len(nb)-i-1)
    return rep
assert convertion_Base10("2221",3)==79
assert convertion_Base10("4F",16)==79
assert convertion_Base10("5123",6)==1131

def convertion_Base4_shadock(nb):
    '''Cette fonction prend en parametre un entier qui est nombre en base 4 et renvoie une chaine.'''
    nb = str(nb)
    rep=""
    for i in nb :
        if i == '0' :
            rep +='GA'
        elif i == '1' :
            rep +='BU'
        elif i == '2' :
            rep +='ZO'
        elif i == '3' :
            rep +='MEU'         
    return rep
assert convertion_Base4_shadock(2100)=="ZOBUGAGA"
assert convertion_Base4_shadock(1)=="BU"
assert convertion_Base4_shadock(11)=="BUBU"

def interface():
    """
    Cette fonction ne prend en argument aucun paramètre et affiche le nombre convertit.
    """
    #Base de départ
    basedepart = input("Donnez la base de départ : ")
    #Le nombre à convertir
    nombre = input("Donnez le nombre à convertir : ")
    #La base dans laquel le nombre sera convetit
    base = input("Donnez la base dans lequel le nombre doit être converti : ")
    #La réponse
    rep = ""
    
    if basedepart == 's' :
        #Si le nombre rentré est en shadock
        rep = converts(nombre)
        rep = convertion_Base10(rep,4)
        rep = convertir_Base_n(rep, base)
        print(rep)
        return None
    elif base == 's' :
        #Si le nombre rentré doit être convertit en shadock
        rep = convertion_Base10(nombre, basedepart)
        rep = convertir_Base_n(rep, 4)
        rep = convertion_Base4_shadock(rep)
        print(rep)
        return None
    else : 
        #Pour les autres bases
        rep = convertion_Base10(nombre, basedepart)
        rep = convertir_Base_n(rep, base)
        print(rep)
        return None

#Démarrage de la fonction
interface()
