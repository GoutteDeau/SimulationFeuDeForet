####################################
### Simulation d'un feu de forêt ###
### arbre = vert                 ###
### arbre en feu = rouge         ###
### cendre = gris                ###
####################################

import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.ndimage import label


##############################
## Fonctions                ##
##############################

def affichage(simulation) :
    dim = (longeur*facteur, hauteur*facteur)
    simulation = cv2.resize(simulation, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("simulation", simulation)

def bruleCase(x, y):
    global simulation
    if simulation[y, x, 0] == vert[0] :
        brule = np.random.randint(0, 101)/100
        if brule <= p:
            simulation[y, x] = rouge

def propagationFeu(x, y):
    global simulation
    if x > 0 :
        bruleCase(x-1, y)
    elif x <= 0 :
        bruleCase(longeur-x-1, y)
    if x < longeur-1 :
        bruleCase(x+1, y)
    elif x >= longeur-1:
        bruleCase(0, y)
    if y > 0 :
        bruleCase(x, y-1)
    elif y <= 0 :
        bruleCase(x, hauteur-y-1)
    if y < hauteur-1 :
        bruleCase(x, y+1)
    elif y >= hauteur-1:
        bruleCase(x, 0)
    simulation[y, x] = gris

def propagationGlobal() :
    feu = np.where(simulation[:, :] == rouge[0])[:2]
    for i in range(len(feu[0])) :
        y = feu[0][i]
        x = feu[1][i]
        propagationFeu(x, y)


def setFire(event, x, y, flags, data) :
    global simulation
    x = x//facteur
    y = y//facteur
    if event == cv2.EVENT_LBUTTONDOWN:
        if simulation[y, x, 0] == vert[0]:
            simulation[y, x] = rouge


def infoSimu(simulation) :
    nb_arbre_brule = len(np.where(simulation[:, :, 0] == gris[0])[0])

    arbre_res = np.zeros(simulation.shape[:2])
    cendre_res = np.zeros(simulation.shape[:2])

    arbre_res[simulation[:, :, 0]==vert[0]] = 1
    cendre_res[simulation[:, :, 0]==gris[0]] = 1
    
    labels_arbre, nb_bloc_arbre = label(arbre_res)
    labels_cendre, nb_bloc_cendre = label(cendre_res)
    
    count_arbre = np.bincount(labels_arbre.ravel())
    count_cendre = np.bincount(labels_cendre.ravel())
    if len(count_arbre) <= 1:
        gros_bloc_arbre = 0
    else:
        gros_bloc_arbre = np.max(count_arbre[1:])
    if len(count_cendre) <= 1:
        gros_bloc_cendre = 0
    else:
        gros_bloc_cendre = np.max(count_cendre[1:])
    print("\n- - - - - - - - - - - - - - - - - - - - - -")
    print("Nombre d'arbres brulé :", nb_arbre_brule)
    print("Nombre de zone d'arbres brulés :", nb_bloc_cendre)
    print("Plus gros bloc d'arbres brulés :", gros_bloc_cendre)
    print("Nombre de zone d'arbres non brulés :", nb_bloc_arbre)
    print("Plus gros bloc d'arbres non brulés :", gros_bloc_arbre)
    print("- - - - - - - - - - - - - - - - - - - - - -")


def init_simulation(bordure, simulation=None):
    sim = simulation
    if simulation is None:
        sim = np.zeros((hauteur, longeur, 3), dtype=np.uint8)
    sim[:] = vert
    if bordure:
        sim[:, 0] = bleu
        sim[:, -1] = bleu
        sim[0, :] = bleu
        sim[-1, :] = bleu
    return sim


##############################
## Paramètres               ##
##############################

p = 0.5
bordure = True
hauteur, longeur = 125, 250
facteur = 4
rouge = [41, 25, 162]
vert = [43, 164, 6]
gris = [100, 100, 100]
bleu = [167, 40, 13]
commandes = (
    "\n"
    " - 'echap' termine la simulation\n"
    " - 'r' recommence la simulation\n"
    " - 'a' affiche les statistiques de la simulation"
)


simulation = init_simulation(bordure)

cv2.namedWindow("simulation")
cv2.setMouseCallback("simulation", setFire)
affichage(simulation[:])
print(commandes)


##############################
## Main               ##
##############################

boucle = True
while boucle:
    propagationGlobal()
    affichage(simulation)
    key = cv2.waitKey(10) & 0x0FF
    if key==27 or key==ord(" "):
        cv2.destroyWindow("simulation")
        boucle = False
    if key==ord("r"):
        simulation = init_simulation(bordure, simulation)
        print(commandes)
    if key==ord("a"):
        infoSimu(simulation)
        img_plot = cv2.cvtColor(simulation, cv2.COLOR_BGR2RGB)
        plt.imshow(img_plot)
        plt.show()
        print(commandes)