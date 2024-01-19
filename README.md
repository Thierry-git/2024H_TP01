# TP1 : Introduction aux Fondamentaux de la Programmation en Python

- [TP1 : Introduction aux Fondamentaux de la Programmation en Python](#tp1--introduction-aux-fondamentaux-de-la-programmation-en-python)
  - [Introduction](#introduction)
  - [Objectifs](#objectifs)
  - [01. Exploration Intergalactique ](#01-exploration-intergalactique-)
  - [02. La Boutique de Baguettes Magiques d'Ollivander](#02-la-boutique-de-baguettes-magiques-dollivander)
  - [03. L'Ingénieur Romain](#03-lingénieur-romain)
  - [04. Le Cryptogramme de l'Alliance Rebelle](#04-le-cryptogramme-de-lalliance-rebelle)
  - [05. Le Système Énergétique de Stark Industries](#05-le-système-énergétique-de-stark-industries)
  - [06. La Batmobile de Bruce Wayne](#06-la-batmobile-de-bruce-wayne)
  - [Exécution des Tests Unitaires](#exécution-des-tests-unitaires)
  - [Remise du travail](#remise-du-travail)
  - [Barème](#barème)
  - [Annexe: Guide et normes de codage](#annexe-guide-et-normes-de-codage)

⏰ Date de remise le Dimanche 11 février 23h59

## Introduction
Bienvenue dans le premier travail pratique de votre parcours d'apprentissage en programmation Python ! Ce TP est conçu pour vous guider à travers les concepts fondamentaux de la programmation. En explorant divers scénarios captivants allant de l'exploration intergalactique à la gestion d'une boutique de baguettes magiques, vous apprendrez à manipuler des variables, à comprendre différents types de données, à utiliser des opérateurs et à construire des expressions. Vous découvrirez également comment les chaînes de caractères fonctionnent en Python et comment les structures de contrôle telles que les instructions 'if' peuvent influencer le flux d'exécution de vos programmes. Chaque exercice est conçu pour renforcer votre compréhension et votre maîtrise des bases de la programmation, vous préparant ainsi à des défis plus complexes dans le futur. 

![TP1](./assets/cover.webp)

<p align="left"> <i>Crédits: <a href="https://openai.com/blog/dall-e/">DALLE 3</a></i></p>

## Objectifs
- Maîtriser les bases de la programmation en Python, notamment les variables, types de données, opérateurs et expressions.
- Comprendre et utiliser efficacement les chaînes de caractères et les opérations associées.
- Apprendre à contrôler le flux d'exécution d'un programme à l'aide de structures de contrôle, telles que les instructions 'if'.
- Développer une capacité à résoudre des problèmes pratiques en utilisant des concepts de programmation de base.

## 01. Exploration Intergalactique <a name="Ex01"></a>

Vous êtes un explorateur parcourant l'univers à la recherche de nouvelles découvertes. Pour partager vos aventures avec le reste de l'univers, vous tenez le fameux blog intergalactique intitulé "Le Journal des Astres". Afin de simplifier la saisie de vos découvertes et de les publier automatiquement sur votre blog, vous décidez de créer un programme informatique. Votre tâche est de développer un script Python qui demande des informations sur chaque nouvelle planète que vous explorez et affiche un blog formaté prêt à être publié.

**Consignes :**

- Demandez le nom de la planète explorée.
- Sollicitez la date de la visite (format JJ/MM/AAAA).
- Demandez une description de la planète.
- Formatez et affichez un message annonçant la nouvelle publication sur le blog, incluant les détails fournis.

**Conseil:** Utilisez le formatage de chaînes pour organiser les informations de manière claire et professionnelle.

**Exemple:**

| Sorties | Entrées  |
|:-----|:--------|
| Entrez le nom de la planete exploree:  | Terre|
| Entrez la date de votre visite (JJ/MM/AAAA):  | 01/01/3000 |
| Decrivez la planete:  | Une planete bleue et verte abritant une multitude de formes de vie.|
| Votre exploration a ete ajoutee au Journal des Astres !<br>-------------------------------<br>Titre : Decouverte de Terre<br>Date : 01/01/3000<br>Description : Une planete bleue et verte abritant une multitude de formes de vie. | |

## 02. La Boutique de Baguettes Magiques d'Ollivander

Vous êtes apprenti chez Ollivander, le célèbre fabricant de baguettes magiques. Afin de gérer efficacement les stocks de matériaux nécessaires à la fabrication des baguettes, vous avez décidé de créer un programme informatique. Votre mission est de développer un script qui calcule les quantités de matériaux nécessaires pour fabriquer un nombre donné de baguettes magiques.

**Consignes :**

- Demandez à l'utilisateur le nombre de baguettes à fabriquer.
- Calculez les quantités nécessaires pour chaque ingrédient : bois, cœurs de créatures magiques et vernis. Par exemple, pour fabriquer une baguette, vous avez besoin de 3 pièce de bois, 1 cœur de créature magique et 10 ml de vernis.
- Affichez les quantités totales de chaque matériau requis.

**Exemple :**

| Sorties | Entrées  |
|:-----|:--------|
| Nombre de baguettes a fabriquer : | 15 |
| Voici les materiaux requis pour la fabrication de 15 baguettes magiques:<br>- 45 piece(s) de bois<br>- 15 coeur(s) de creatures magiques<br>- 150 ml de vernis | |

## 03. L'Ingénieur Romain

Félicitations ! Vous avez été nommé l'unique ingénieur du camp romain aux abords du village d'Astérix et Obélix. Votre mission est de calculer la portée des catapultes pour le prochain "grand" assaut (le précédent ayant été un fiasco mémorable). Les catapultes, récemment rénovées après l'incident impliquant un sanglier volant et un centurion malchanceux, sont prêtes à l'emploi.  Vous devez maintenant écrire un script pour prédire la distance que chaque rocher lancé par les catapultes peut atteindre.

**Consignes :**
- Demandez au légionnaire de service (qui a l'air plutôt nerveux) de vous fournir la vitesse initiale et l'angle de lancement pour chaque catapulte. 
- Appliquez vos compétences en mathématiques (et en prières aux dieux romains) pour calculer la distance que le projectile peut parcourir. Utilisez la formule de la portée d'un projectile : 
$$D = \frac{vitesse^2 \times \sin(2 \times angle)}{g}$$
où g est l'accélération due à la gravité ($\ 9,81 m/s^2$).
- Présentez vos résultats avec assurance (et un peu d'espoir) pour déterminer si le village gaulois est à portée (arrondies à deux décimales près).

**Note 1 :** Pour utiliser la fonction sinus, vous devez importer le module `math`.

**Note 2 :** La fonction sinus prend en paramètre un angle en radians. Il est donc nécessaire de convertir l'angle.

**Exemple :**

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez la vitesse initiale (en m/s) :  | 20.5 |
| Entrez l'angle de lancement (en degres) :  | 30 |
| La distance parcourue par le projectile est de 37.10 metres.  |  |

## 04. Le Cryptogramme de l'Alliance Rebelle

En tant que membre de l'Alliance Rebelle, vous vous trouvez face à une tâche de cryptographie unique : déchiffrer un message crypté de l'Empire. Ce message, bien qu'apparemment ordinaire, cache en réalité des informations vitales. Selon les experts en cryptographie, les occurrences des voyelles dans le texte pourraient indiquer des coordonnées précises dans la galaxie, indiquant potentiellement l'emplacement d'une base stratégique de l'Empire.

Vous avez été chargé de déterminer ces coordonnées secrètes en comptant le nombre d'occurrences des voyelles "a", "e", "i", "o", "u" et "y" dans le message. Chaque nombre correspondra à une partie des coordonnées galactiques. Par exemple, si le message contient 4 "a", 6 "e", 3 "i", 5 "o", 3 "u" et 0 "y", les coordonnées galactiques seraient "4.6.3.5.3.0".

**Consignes :**
1. Saisissez le message crypté envoyé par l'Empire.
2. Analysez le message pour compter séparément le nombre d'occurrences des voyelles "a", "e", "i", "o", "u" et "y".
3. Assemblez les résultats sous la forme d'une coordonnée galactique : "123.13.123.12.11.1", où chaque nombre représente les occurrences de "a", "e", "i", "o", "u" et "y", dans cet ordre, séparés par des points.
4. Affichez les coordonnées complètes, qui pourraient mener à la découverte d'une base secrète impériale.

**Exemple :**

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le message de l'Empire :  | La force est avec vous, mais l'Empire est partout! |
| Les coordonnees galactiques sont 4.6.2.3.2.0. |  |

## 05. Le Système Énergétique de Stark Industries

En tant qu'ingénieur chez Stark Industries, vous avez été chargé de développer un nouveau système de surveillance pour les réacteurs Arc. Ce système doit non seulement afficher le niveau actuel de charge de la batterie, mais aussi alerter en cas de charge anormale, pour prévenir tout risque de surcharge ou de défaillance énergétique. Vous devez créer un système d'alerte qui indique visuellement le niveau de charge de la batterie et affiche un message d'erreur si la charge est en dehors de la plage normale (0 à 100%).

**Consignes :**
1. Demandez à l'utilisateur d'entrer le niveau de charge actuel de la batterie (en pourcentage).
2. Si le niveau de charge est entre 0 et 100%, affichez une représentation graphique de la charge de la batterie. Chaque barre représente 10% de charge, et le pourcentage doit être arrondi à la dizaine la plus proche pour déduire le nombre de barres. Utilisez le caractère suivant: `❚`.
3. Si le niveau de charge est négatif ou supérieur à 100%, affichez un message d'erreur.

**Note :** Pour faciliter la création de la barre de progression, utilisez l'opérateur de multiplication sur les chaînes de caractères. Pour plus d'informations sur cette fonctionnalité, consultez cette [documentation](https://www.geeksforgeeks.org/create-multiple-copies-of-a-string-in-python-by-using-multiplication-operator/).

**Exemples :**

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le niveau de charge actuel de la batterie :  | 0 | 
| [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]</br>0% |  |

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le niveau de charge actuel de la batterie : | 12 | 
| [❚&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]</br>12%  | |

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le niveau de charge actuel de la batterie :  | 68 | 
| [❚❚❚❚❚❚❚&nbsp;&nbsp;&nbsp;]</br>68% |  |

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le niveau de charge actuel de la batterie :  | 123 | 
| Erreur : niveau de charge invalide. |  |

## 06. La Batmobile de Bruce Wayne

Dans l'univers de Gotham City, vous incarnez le légendaire Batman, et votre précieuse Batmobile est votre principal atout dans la lutte contre le crime. Cependant, pour être prêt à intervenir à tout moment, il est crucial de surveiller la durée de vie restante de la batterie de la Batmobile. Votre mission consiste à écrire un programme qui calcule le temps restant de la batterie de la Batmobile, en fonction du pourcentage de charge actuel.

**Consignes :**

- Demandez à l'utilisateur de saisir le pourcentage de charge actuel de la batterie de la Batmobile.
- Vérifiez si le pourcentage est valide, c'est-à-dire s'il est compris entre 0% et 100%. Si ce n'est pas le cas, affichez un message d'erreur approprié et quittez le programme.
- Calculez le temps restant en minutes en fonction du pourcentage de charge, en utilisant les règles suivantes :
    - Si le pourcentage est de 100% à 51%, chaque pourcentage équivaut à 1 minute.
    - Si le pourcentage est de 50% à 6%, chaque pourcentage équivaut à 2 minutes.
    - Si le pourcentage est de 5% à 0%, chaque pourcentage équivaut à 5 minutes.
- Affichez le temps restant au format "XhYYmin", où X est le nombre d'heures et Y est le nombre de minutes.

**Exemples :**

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le pourcentage de charge actuel de la batterie de la Batmobile : | 100 |
| Temps restant : 2h45min |  |

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le pourcentage de charge actuel de la batterie de la Batmobile :|  42 |
| Temps restant : 1h39min |  |

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le pourcentage de charge actuel de la batterie de la Batmobile : |  1 |
| Temps restant : 0h05min | |

| Sorties |  Entrées  |
|:------|:-----------|
| Entrez le pourcentage de charge actuel de la batterie de la Batmobile :  | 142 |
| Erreur : niveau de charge invalide. | |

## Exécution des Tests Unitaires

Pour garantir la conformité de vos scripts aux exigences des exercices, exécutez le fichier `tests_tp1.py`. Ces tests unitaires vérifient que chaque exercice fonctionne correctement et produit les résultats attendus. Exécutez ce fichier dans votre environnement de développement pour tester vos scripts avant la soumission.

## Remise du travail

Pour soumettre votre travail, créez un fichier zip nommé `LXX-YY-TP1.zip`, où `XX` est le numéro de votre section de laboratoire et `YY` le numéro de votre équipe (par exemple, `L02-04-TP1.zip` pour la section 02, équipe 04). Incluez dans ce zip vos scripts `exo1.py` à `exo6.py`. Assurez-vous que chaque script fonctionne correctement et déposez le fichier zip dans la boîte Moodle du TP correspondant à votre section. Aussi, assurez-vous d'exécuter le fichier `tests_tp1.py` pour valider vos solutions avant de soumettre le fichier zip.

## Barème

| Question | Points |
| -------- | ------ |
| 1      | 2      |
| 2      | 3      |
| 3      | 4      |
| 4      | 3      |
| 5      | 3      |
| 6      | 5      |
| **Total**| **20**|

## Annexe: Guide et normes de codage
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. Vous avertis aussi si vous ne respectez pas certaines de normes de PEP8, le guide de codage officiel de Python.
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)