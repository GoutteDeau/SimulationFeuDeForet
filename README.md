# Simulation d'un feu de forêt

Projet de simulation en Python modélisant la propagation d'un feu de forêt sur une grille.

La simulation représente différents états :

* **Vert** : arbre non brûlé
* **Rouge** : arbre en feu
* **Gris** : arbre brûlé / cendre
* **Bleu** : bordure de la simulation

L'utilisateur peut déclencher un incendie en cliquant directement sur un arbre dans la fenêtre de simulation.


## Sommaire

* [Fonctionnement](#fonctionnement)
* [Paramètres](#️paramètres)
* [Commandes](#commandes)
* [Statistiques](#statistiques)
* [Technologies utilisées](#technologies-utilisées)
* [Installation](#installation)
* [Lancer la simulation](#lancer-la-simulation)
* [Résultats et analyse](#résultats-et-analyse)
* [Fonctionnalités possibles à ajouter](#-fonctionnalités-possibles-à-ajouter)
* [Auteur](#auteur)


---

## Fonctionnement

La forêt est représentée sous la forme d'une grille de pixels composée d'arbres.

Lorsqu'un arbre est en feu, celui-ci peut propager l'incendie à ses voisins selon une probabilité définie par le paramètre `p`.

Une fois qu'un arbre a propagé le feu, il devient une zone brûlée.

La simulation permet également d'obtenir différentes statistiques sur l'état de la forêt.

---

## Paramètres

Les principaux paramètres de la simulation peuvent être modifiés directement dans le code :

```python
p = 0.5                 # Probabilité de propagation du feu
bordure = True          # Activation des bordures
hauteur, longeur = 125, 250  # Dimensions de la simulation
facteur = 4             # Facteur d'agrandissement de l'affichage
```

---

## Commandes

| Touche              | Action                     |
| ------------------- | -------------------------- |
| Clic gauche         | Met le feu à un arbre      |
| `R`                 | Réinitialise la simulation |
| `A`                 | Affiche les statistiques   |
| `Échap` ou `Espace` | Quitte la simulation       |

---

## Statistiques

La simulation permet d'obtenir plusieurs informations :

* Nombre total d'arbres brûlés.
* Nombre de zones d'arbres brûlés.
* Taille de la plus grande zone brûlée.
* Nombre de zones d'arbres non brûlés.
* Taille de la plus grande zone d'arbres non brûlés.

Les zones sont détectées à l'aide d'un algorithme d'étiquetage des composantes connexes.

---

## Technologies utilisées

* **Python**
* **NumPy**
* **OpenCV**
* **Matplotlib**
* **SciPy**

---

## Installation

Clonez le repository :

```bash
git clone https://github.com/VOTRE-PSEUDO/NOM-DU-REPOSITORY.git
```

Accédez au dossier :

```bash
cd NOM-DU-REPOSITORY
```

Installez les dépendances :

```bash
pip install numpy opencv-python matplotlib scipy
```

---

## Lancer la simulation

Exécutez simplement le fichier Python :

```bash
python simulation.py
```

Une fenêtre contenant la simulation devrait alors s'ouvrir.

Cliquez sur un arbre pour déclencher un incendie.

---

## Résultats et analyse

Une analyse des résultats obtenus lors des simulations est disponible dans le fichier : [analyse des résultats](ANALYSE.md)


## 💡 Fonctionnalités possibles à ajouter

* Ajout du vent pour influencer la propagation du feu.
* Génération aléatoire de la forêt.
* Obstacles naturels (rivières, routes, zones rocheuses).
* Différents types d'arbres avec des probabilités de combustion différentes.
* Graphiques montrant l'évolution du feu au cours du temps.
* Sauvegarde des résultats de simulation.
* Interface permettant de modifier les paramètres sans toucher au code.

---

## Auteur

**Malo Etienne**

Étudiant en deuxième année du cycle ingénieur à l'ESIR (Option Imagerie Numérique)
