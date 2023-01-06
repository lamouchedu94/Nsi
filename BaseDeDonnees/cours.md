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

## II/Base de donnée 

Avec l'invention du disque dur en 1956, par IBM (5mb) la capacité de stockage des ordinateurs augmente considérablement et n'est plus nécésairement séquentielle.
Le terme database apparait en 1964 pour désigner une collection d'info partagé entre différents utilisateurs. Il existe différent moyens d'organiser les données
le plus répendu = Bdd relationnelle qui sont une implémentation du model relationnel. Il existe d'autre types de base qui répondent é des besoins
spécifiques comme les bases multidimentionnelle par ex. Avec l'explosion des capacité de stockage et du volume de donnée (web, big data...) les bases de données
sont é présent des outils incontournables. 

### A) Systeme de gestion de bases de données

L'enssemble des opérations liées aux données (stockage, écrtiture, lecture, modification, droit d'accés...) se qui fait é l'aide d'un systéme de gestion de 
base de donnée (appelé SGBD). Il existe différent SGBD, comerciaux (payant) Oracle, Microsoft Sql server... ou bien libre MariaDb, Sqlite, Postgrey Sql...
Ils sont tous basés sur le méme langage : Structured Query Language (sql) mais les implémentations peuvent présenter des différences qui obligerai é 
revoir le code en détail pour passer d'un systeme é l'autre. Il est é noter que l'utilisateur n'a aucun moyen de savoir comment les données sont stockées
il ne peut que passer par l'intermédiaire du SGBD. Le SGBD propose un contrat é l'utilisateur qui lui garantit un certain nombre de fonctionnalités sans 
rentrer dans le détail de l'implémentation. Un SGBD permet de :
- Gerer la lecture, l'écriture ou la modification d'info contenues dans la Base de Donnée
- Gerer les autorisations d'accés é la base de donnée
- Gerer la duplication de la base de donnée faire en sorte que les fichiers soient placé é plusieurs endroits pour les sauvgarder
- Assurer des accés concurent é la base de donnée (plusieurs utilisateurs peuvent l'utiliser en méme temps

A titre d'exemple nous shouaiton modéliser un lycée simplifié. 2 classes de 3 éléves. Dans chaque classe 2 enseignement Science et Lettres et le lycée comporte 2 prof
de science et 2 prof de lettre.

1ére tentative : 
Nom | Prenom | Classe | Nom_prof | Prenom_Prof | Matiére

Pas solution satisfaisante plusieurs info répétées se qui rend le tableau peu lisible. De plus saisie trés compliquée augmentant le risque d'erreur sans compter
la dificultée de certaines modifications (ex changement prof / éléve). D'une maniére générale,  on s'attachera é la création d'une BDD toute redondance de données.
L'idée pour cela sera souvent de créer plusieurs table que l'on pourra mettre en relation les unes avec les autres. 

### B) Représentation d'une BDD

Une BDD relationnelle est l'implémentation d'un enssemble de relation. Une relation peut étre vue comme en tableau é deux dimenssions 

Lors de la création d'une tables il faut définir leurs différents attributs et leurs domaines (cad le type de donnée stocké). Chaque enrengistrement est alors une 
tuple, comportant autant d'éléments qu'il y a d'attribut dans la table du bon type. Une table ne peu contenir 2 enrengistrment identique, pour cela on définit 
généralement une clef primaire. Une clef primaire est un atribut ou un groupe d'attribut dont la valeur permet d'identifier de maniére unique un enrengistrement de
la table. Elle assure donc l'unicité des enrengistements de la table.

### Quelques commandes sql

- CREATE TABLE eleve (nom VARCHAR(255), classe INT, id SERIAL PRIMARY KEY);
- CREATE TABLE matiere (intitule VARCHAR(255), id SERIAL PRIMARY KEY);
- CREATE TABLE note (id_eleve INT REFERENCES eleve(id), id_matiere INT REFERENCES matiere(id), moyenne INT, PRIMARY KEY (id_eleve, id_matiere));

```sql
select eleve.nom,eleve.prenom,note.moyenne,prof.nom,matiere.intitule from note
join matiere on matiere.id = note.id_matiere
join eleve on note.id_eleve = eleve.id
join prof on prof.num_classe = eleve.classe and matiere.id = prof.id_matiere
```

# Types d'atributs :
- SmallInt (entier 16 bits avec un signe)
- Int (entier 32 bits avec signe)
- BigInt (entier 64 bits avec signe) 
- Decimal(t,f) (décimal signé de t chiffre dont f après la virgule)
- Real (flotant sur 32 bits)
- Double (flotant sur 64 bits)

---

- Char(n) chaine de n caractère (si il en manque complté par des espaces)
- VarChar(n) Chaine d'au plus n caractère
- Text chaine de n'importe qu'elle longueur

---

- Date : AAAA-MM-JJ
- Time : HH:MM:SS
- Timestamp : AAAA-MM-JJ HH:MM:SS

--- 

- SERIAL : dans le cas de postgre, entier qui s'incrémente automatiquement à chaque nouvel enrengistrement

La constante Null à tous les types possible

Si on veut interdire à l'utilisateur d'utiliser Null rajouter "NOT NULL" lors de la création de la table. Ex : 
```sql
CREATE TABLE exemple(nom VARCHAR NOT NULL);
CREATE TABLE client(id SERIAL PRIMARY KEY, nom VARCHAR NOT NULL, age SMALLINT, CHECK(age>=0 AND age <= 150));
DROP TABLE exemple;  '(possible uniquement si aucune celf étrangère d"une autre table ne pointe une clef primaire de cette table.)'
CREATE TABLE voiture(immatriculation VARCHAR(10) PRIMARY KEY, marque VARCHAR(255), modele VARCHAR(255), proprietaire INT REFERENCES client(id));
```

```sql 
INSERT INTO client (nom,age) VALUES ('Martin', 27), ('Alice', 71), ('Bob', 74);
INSERT INTO voiture (immatriculation, marque, modele, proprietaire) VALUES ('AB123CD', 'Ferrari', 'F456', 1);
INSERT INTO voiture (immatriculation, marque, modele, proprietaire) VALUES ('EF456GH', 'Mercedes', 'classe E', (SELECT id FROM client WHERE nom='Alice'));
INSERT INTO voiture (immatriculation, marque, modele, proprietaire) VALUES ('IJ789KL', 'Lada', '2107', (SELECT id FROM client WHERE nom='Bob'));
INSERT INTO voiture (immatriculation, marque, modele, proprietaire) VALUES ('EF458GH', 'Mercedes', 'classe S', (SELECT id FROM client WHERE nom='Alice'));

'Changement de proprio :'
UPDATE voiture SET proprietaire=(SELECT id FROM client WHERE nom='Bob');

'Avoir tous les proprio de Mercedes :'
SELECT nom FROM client WHERE id IN (SELECT proprietaire FROM voiture WHERE marque='Mercedes')

'Sup Mercedes:'
DELETE FROM voiture WHERE marque='Mercedes'


SELECT client.nom, voiture.marque, voiture.modele FROM voiture JOIN client ON voiture.proprietaire=client.id;

SELECT DISTINCT marque FROM voiture;

SELECT immatriculation FROM voiture ORDER BY immatriculation ASC;

SELECT * FROM voiture WHERE immatriculation LIKE '%12%';
SELECT * FROM voiture WHERE immatriculation LIKE '_B__3_D';
```

On appel shéma relationnel l'enssemble des relations présente dans une bdd. Quand on demande le shéma relationnel d'une base de données, il faut donner le nom des différentes relations, avec leurs attributs (et leur type), en précsant les clefs primaires et clefs étangère lorsqu'il y en a.

Nous adopterons la convention suivante : lorsqu'on écrit le shéma d'une base la clef primaire est l'attribut dont le nom est souligné dans le shéma, les nom d'attributs qui sont des clefs étrangères sont précédés par un #. (Attention : Ce n'est pas la syntaxe que l'on utilise dans l'implémentation de la base, ça permet simplement de proposer un schéma facilement lisible.)

Par convention, les mots liés a langage sont en majuscules, les autres en minuscules. On met les noms de relations au singulier. 

A chaque fois qu'on modifie ou ajoute un enrengistrement à une base de donnée, le SGBD effectue divers contrôles, pour s'assurer de l'intégrité des données. Ce qui permet par exemple d'éviter cetaines erreurs de saisie. Ces contrôles dépendent de ce qui a été indiqué lors de la création de la base via ce que l'on appelle les contraites (d'intégrité).


Le langage SQL comporte des fonctions qui peuvent calculer un résultat en fonctions des valeurs d'une colonne de la table. On les appelle des fonctions d'agrégation. Par exemple, MIN,MAX,AVG (moyenne), COUNT (renvoie le bombre d'enrengistrements selectionnés). 
```sql 
SELECT COUNT(*) FROM voiture WHERE marque='Mercedes';
SELECT MAX(id) FROM client 
```



## SQL MURDER MYSTERY
```sql
select * from crime_scene_report where type IN (SELECT type FROM crime_scene_report WHERE type='murder') 
AND date IN (select date FROM crime_scene_report where date=20180115)
AND city IN (select city FROM crime_scene_report where city="SQL City"); ;

select * from person where id IN (SELECT id from person where address_street_name= "Franklin Ave"); 

select name, address_number from person where address_street_name in (select address_street_name from person where address_street_name="Northwestern Dr") order by address_number DESC; 

select * from get_fit_now_member where membership_status in 
(select membership_status from get_fit_now_member where membership_status ='gold');

select * from drivers_license where id in (select license_id from person where name='Jeremy Bowers');

```

Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave".


16371	Annabel Miller	490173	103	Franklin Ave	318771143

16371	I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th.

### Structure de données

#### crime_scene_report : 
- date : 20180115 	
- type : robbery/murder/theft/fraud
- description :    
- city : 
#### drivers_license
- id : 100280
- age : 72
- height : 	
- eye_color :	
- hair_color :	
- gender :
- plate_number : P24L4U
- car_make :
- car_model :
#### facebook_event_checkin
- person_id : 28508
- event_id : 5880
- event_name :
- date : 20170913
#### interview 
- person_id	: 28508
- transcript
#### get_fit_now_member
- id :
- person_id :
- name :
- membership_start_date :
- membership_status :
#### get_fit_now_check_in
- membership_id
- check_in_date
- check_in_time
- check_out_time
#### income
- ssn :
- annual_income :
#### person
- id : 14887
- name : Morty Schapiro
- license_id : 118009
- address_number : 4919
- address_street_name : Northwestern Dr
- ssn : 111564949

I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W".

48Z7A	28819	Joe Germuska	20160305	gold
48Z55	67318	Jeremy Bowers	20160101	gold

---
## EN presque une ligne
```sql 
select name, MAX(address_number) from person where address_street_name in 
(select address_street_name from person where address_street_name="Northwestern Dr") 
order by address_number DESC; 

select * from interview where person_id in (select id from person where name = 'Morty Schapiro');

select * from drivers_license where id in (select license_id from person where name in (select name from get_fit_now_member where id like '%48Z%' and membership_status='gold'));

select * from person where license_id=423327;
```
```sql
SELECT groupes.nom FROM groupes JOIN concerts ON groupes.idgrpe=concerts WHERE concerts.scene=1;
```