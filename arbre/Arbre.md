# Arbre binaire 
Un arbre binaire est un enssemble fini de noeud correspondant à l'un des deux cas suivant : 
- Arbre vide (aucun noeud)
- Soit l'arbre n'est pas vide et ses noeud sot structuré de la façon suivante :
    - Un noeud est appelé la racine de l'arbre
    - les noeuds restants sont séparés en 2 sous enssembles qui forment récusivement deux sous arbres appelés sous arbre Gauche et Sous arbre Droit
    - la racine est relié à la racine de chacun de ces sous arbre (lorsqu'ils ne sont pas vide)

La taille d'un arbre binaire est le nombre de noeud qu'il contient. 
## Photo Papier
Un noeud dont les 2 sous arbres sont vide s'appel une feuille

La Hauteur d'un arbre : Le plus grand nombre de noeud rencontrés en déscendant de la racine jusqu'à une feuille

Taille d'un arbre :
- 0 si l'arbre est vide 
- 1 + taille (sous arbre Gauche) + taille (sosu arbre Droit) sinon 

Hauteur d'un arbre :
- 0 si l'arbre est vide
- 1 + maximum (hateur (sous arbre gauche), hauteur(sous arbre droit)) Sinon 

Dans un arbre de hauteur h on peut avoir un maximum 2⁰+2¹+2²+2³+...+ 2^h-1 noeuds

Premier terme 1 - la raison puissance n de terme sur 1 - la raison 

Un arbre dont tous les sous arbre non vide sont des sous arbre droit ou gauche s'appel un peigne.

Un arbre dont toutes les feuilles sont exactement à la même profondeur, s'appel un arbre parfait. Un arbre parfait de hauteur h comporte 2^h-1 noeuds

Pour stocker de l'info dans un arbre, on peut attacher une valeur à chaque noeud. 

Parcourir un arbre c'est passer une et une seule fois par chaque noeud de l'arbre. On distingue plusieurs parcours :
- Préfix :
    - On note la val de la racine 
    - Parcour Préfix du sous arbre G   
    - Puis Parcours de sous arbre D
- Infix :
    - Parcour infix du ss arbre G
    - On note valeur de la racine
    - Parcour infix du ss arbre G
- Postfix 
    - Parcour Postfix du ss arbre G
    - Parcour Postfix du ss arbre D
    - Puis note valeur de la racine
    
Implémenter taille et hauteur. Parcour Infix.