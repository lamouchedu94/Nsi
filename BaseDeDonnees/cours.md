modèle realationnel :
## I/    
un modèl ede donnés est une représentation (math ou info) de concepts que l'on souhaite étudier. Un modèle permet d'enoncer des proriétés de ces données en terme logique. Il permet aussi de programer des processus sous forme d'opération élémentaire sur les données. Ex gestion bibliothèque. L'un des modèles de donnés le plus populaire est le modèle relationnel pour info ce dernier a été définit en 1970 par Edgard Frank codd (américain), (1923-2003) chez IBM. Dans ce modèle un objet modélisé est représenté par un n uplet de valeur et les collections d'objets par des enssembles de n uplet. Cet enssemble d'n uplet sappel une relation. On l'appel aussi une table.

Chaque relation se conforme à un schéma, ce dernier est une description qui indique pour chaque composant de n uplet leur nom et leur domaine, une telle composante s'appel un atribut ou bien une colone.  

chaque relation se conforme à un schéma. Ce dernier est une description qui indique pour chaque composante des n-uplet 
de la relation leur nom et leur domaine.
 
Une base de donnée est un ensemble de relations. Par extension on appelle schéma d'une base de donnée l’ensemble
des schéma des relations constituant la base. 
 
La modélisation des données se décompose en plusieurs étapes 
- déterminer les entiter (objets, action, personnes...) que l'on souhaite manipuler
- modéliser les ensembles d'entiter comme des relations en donnant leurs schéma en s'attachant en particulier à
choisir le bon domaine pour chaque attribut 
- définir les contraintes de la base de donnée c'est à dire l’ensemble des propriétés logiques que nos données
doivent vérifier à tout moments
 
Contraintes d'intégrité
 
C'est une prorpriété logique préservé à tout instant par la base de donnée et qui garantit la cohérence des données
Il y en a 4 types.
 
chaque attributs doit correspondre au domaine définit lors de la création de la relation
- String 
- Int 
- Boolean
- Float 
- Date jj/mm/aaaa
- Time hh:mm:ss
 
Le choix des domaines et particulièrement imortant car il doit répondre à 2 impératifs :
- Représenter correctement et sans perte d'info toutes les valeurs possible pour un attribut
- Limiter autant que possible la saisie de données illégales ou mal formées (filtrer certaines erreurs)
00 00 00 00 00
 
 
- Contrainte d'entité permet de s'assurer que chaque élément d'une relation est unique et identifie une entité de 
manière non ambigu.
 
Il faut s'assurer lors de la modélisation, que pour chaque entité d'une relation un attribut ou un ensemble 
d'attribut permet d'identifier cette entité de manière unique. Souvent on utilisera des identifiants unique pour
assurer cette contrainte d'entité. Lors de la modélisation, il faut choisir l'attribut ou le groupe d'attributs
qui permettra de désigner une donnée de manière unique. On appelle ça clef primaire de la relation. On l'indique 
en la soulignant.
Donc le choix de la clef primaire est important car le système garantira son unicité pour préserver la contrainte
d’entité. 
 
Contrainte de référence :
- Une clef primaire d'une relation permet aussi de servir de référence dans une autre relation 
On dit alors que c'est une clef étrangère de la relation
 
 
Contrainte Utilisateurs :
- Ce sont toutes les contraintes d'une relation que l'on ne peut pas exprimer par les 3 précédentes.
