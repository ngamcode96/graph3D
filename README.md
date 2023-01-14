#### NGAM Amadou 12111338
#### FALL Moussa 12012045
#### SARR Serigne Abdou Lat 12014599

### Dépendances
pour tester le code, Tapez cette commande pour installer les dépendances.
pip install -r requirements.txt

### lancer le programme
le fichier root main.py pour lancer le programme

Dans le fichier main.py vous avez plusieurs options

   #### -Tester la visualisation 3D
        -methode optimale (octree et Barnes Hut)
   #### -Tester la visualisation 2D
        -methode optimale (quadtree et Barnes Hut)

Pour la visualisation 3D, vous pouvez utiliser la méthode naive (O(n**2)) pour calculer les forces de répulsion
en utilisant la fonction update_positions_naive()

### Analyse Amortie et Réelle
Vous pouvez aussi activer l'analyse amortie et réelle dans les fonction update_positions() et update_positions_naive() en mettant comme paramètre enable_analyzer=True
les fichiers générés se trouve dans le répertoire /plots.


### Force de répulsion:
F = G*masse1*masse2/distance**2

### Force de attraction:
F = -G/masse

### Constantes
G = 1.5
theta_max = 0.80
dt = 0.05
distance_min = 0.000005
n_iter = 100

