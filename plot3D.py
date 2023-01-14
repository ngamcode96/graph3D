import numpy as np
import matplotlib.pyplot as plt
from node import Node3D
from figure import Cube
from octree import Octree
from forces import *
import time
from analyzer import Analyzer
import networkx as nx

class Plot3D:
    def __init__(self, nodes, edges, G=2.0, theta_max=1.2, distance_min=0.000005, dt=0.06):
        self.nodes = nodes
        self.edges = edges
        self.G = G
        self.theta_max= theta_max
        self.distance_min = distance_min
        self.dt = dt

    #Cette méthode permet de générer aleatoirement des positions(x,y,z) pour les noeuds du graphes.    
    def generate_random_positions_of_nodes(self):
        self.nodes3D = []
        self.index_of_labels = {}
        for index,n in enumerate(self.nodes):
            self.index_of_labels[n] = index 
            position = np.random.uniform(0, 1,3)
            node = Node3D(position[0], position[1], position[2])
            self.nodes3D.append(node)

    
    #cette fonction permet de mettre à jours les positions de chaque après chaque itération 
    # en utilisant un octree pour otimiser les calculs
    def update_positions(self, Graph, G=2.0,theta_max=1.2,dt=0.05, distance_min=0.000005, n_iter=6000, enable_analyzer=False):
        print("Mise à jour des positions...")
        #lorsequ'on souhaite mesurer le cout reel et amorti sur les operations de calculs
        if  enable_analyzer:
            time_analysis_forces_repulsion = Analyzer()
            time_analysis_update_positions = Analyzer()
            time_analysis_insert_octree = Analyzer()

        cube = Cube(np.array([0.0, 0.0, 0.0]), length=4)
        for i in range(n_iter):
            before_i = time.time()
            #pour chaque itération on crée un octree avec de nouvelles positions
            octree = Octree(cube)  

            #pour chaque noeud on initialise à O la vitesse de chaque noeud.
            before_insert_nodes_octree = time.time()  
            for node in self.nodes3D:
                node.velocity_x = 0.0
                node.velocity_y = 0.0
                node.velocity_z = 0.0
                #puis on insert le noeud dans l'octree.
                octree.insert(node)
            after_insert_nodes_octree = time.time()

            if enable_analyzer:
                time_analysis_insert_octree.append(round((after_insert_nodes_octree-before_insert_nodes_octree)*10**9, 6))    

  
            
                
            #on calcule d'abord les forces de repulsions en utilisant l'octree avec l'optimisation de Barnes Hut
            before = time.time()
            for node in self.nodes3D:
                octree.force_replusion_gravity_center_3D(node, G=G,theta_max=theta_max)
            after = time.time()

            if enable_analyzer:
                time_analysis_forces_repulsion.append(round((after-before)*10**9, 6))   

            #Ensuite on calcule les forces d'attraction entre chaque noeud et ses voisins 
           
            for n in Graph.nodes():
                neighbors = nx.neighbors(Graph, n)
                for nei in neighbors:
                    force_attraction(self.nodes3D[self.index_of_labels[n]], self.nodes3D[self.index_of_labels[nei]], G=G, distance_min=distance_min)
           
            #on termine par la mis à jour des position x,y,z
            for ni in Graph.nodes():
                self.nodes3D[self.index_of_labels[ni]].update_position(dt=dt)
            after_i = time.time()
            if enable_analyzer:
                time_analysis_update_positions.append(round((after_i-before_i)*10**9, 6))

            

        


            #on recommence le processus jusqu'a n_iter

        #on enregiste les temps mesurés dans des fichiers dot.
        if enable_analyzer:
            time_analysis_forces_repulsion.save_values("plots/octree_time_insert_nodes.plot")
            self.save_time_analyser_plot("plots/octree_time_insert_nodes.plot", "Temps amorti (Octree) Insertion des noeuds après chaque itération")

            time_analysis_forces_repulsion.save_values("plots/octree_time_forces_replusion.plot")
            self.save_time_analyser_plot("plots/octree_time_forces_replusion.plot", "Temps amorti (Octree) sur les forces de répulsions")
            time_analysis_update_positions.save_values("plots/octree_time_update_positions.plot")
            self.save_time_analyser_plot("plots/octree_time_update_positions.plot", "Temps amorti (Octree) sur après mis à jours des positions du noeud")

    # #ette fonction permet de mettre à jours les positions de chaque après chaque itération 
    # sans optimisation
    def update_positions_naive(self, Graph, G=2.0, dt=0.05, distance_min=0.000005, n_iter=6000, enable_analyzer=False):
        
        #lorsequ'on souhaite mesurer le cout reel et amorti sur les operations de calculs
        if  enable_analyzer:
            time_analysis_forces_repulsion = Analyzer()
            time_analysis_update_positions = Analyzer()

        for i in range(n_iter):
            before_i = time.time()

            #pour chaque noeud on initialise à O la vitesse de chaque noeud.  
            for node in self.nodes3D:
                node.velocity_x = 0.0
                node.velocity_y = 0.0
                node.velocity_z = 0.0
                
            #on calcule d'abord les forces de repulsions en avec la méthode naive(O(n**2))
            before = time.time()
            for node1 in self.nodes3D:
                for node2 in self.nodes3D:
                    force_replusion(node1, node2, G=G)
            after = time.time()

            if enable_analyzer:
                time_analysis_forces_repulsion.append(round((after-before)*10**9, 6))   

            #Ensuite on calcule les forces d'attraction entre chaque noeud et ses voisins 
            for n in Graph.nodes():
                neighbors = nx.neighbors(Graph, n)
                for nei in neighbors:
                    force_attraction(self.nodes3D[self.index_of_labels[n]], self.nodes3D[self.index_of_labels[nei]], G=G, distance_min=distance_min)
                        
            #on termine par la mis à jour des position x,y,z
            for ni in Graph.nodes():
                self.nodes3D[self.index_of_labels[ni]].update_position(dt=dt)
            after_i = time.time()
            if enable_analyzer:
                time_analysis_update_positions.append(round((after_i-before_i)*10**9, 6))

            

        


            #on recommence le processus jusqu'a n_iter

        #on enregiste les temps mesurés dans des fichiers dot.
        if enable_analyzer:
            time_analysis_forces_repulsion.save_values("plots/naive_time_forces_replusion.plot")
            self.save_time_analyser_plot("plots/naive_time_forces_replusion.plot", "Temps amorti sur les forces de répulsions")
            time_analysis_update_positions.save_values("plots/naive_time_update_positions.plot")
            self.save_time_analyser_plot("plots/naive_time_update_positions.plot", "Temps amorti sur après mis à jours des positions du noeud")


#Visualiser les positions des noeuds du graphe et ses aretes
    def plot(self):

        #récupérer les positions des nodes
        positions = {}
        inv_index_of_labels = {v: k for k, v in self.index_of_labels.items()}

        for index,node in enumerate(self.nodes3D):
            positions[inv_index_of_labels[index]] = np.array([node.x, node.y, node.z])


        #construire un vecteur contenant les positions des noeuds
        node_xyz = np.array([positions[v] for v in self.index_of_labels.keys()])

        #construire un vecteur contenant les aretes entre les nodes
        edge_xyz = np.array([(positions[u], positions[v]) for u, v in self.edges])

        fig = plt.figure(figsize=(20,15))
        ax = fig.add_subplot(111, projection="3d")

        #afficher les noeuds
        ax.scatter(*node_xyz.T, s=400, ec="w")

        # Ajouter les noeuds
        for vizedge in edge_xyz:
            ax.plot(*vizedge.T, color="tab:gray")


        #on supprime les valeurs sur les axes
        for dim in (ax.xaxis, ax.yaxis, ax.zaxis):
            dim.set_ticks([])

        
        ax.grid(False)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")
        fig.tight_layout()
        plt.show()

#Visualiser et enregistrer les temps amortis et rééls
    def save_time_analyser_plot(self,dot_file, title):

        file = open(dot_file, 'r')
        fig = plt.figure(figsize=(15, 8))
        plt.title(title)

        x = []
        costs = []
        amortized_time = []
        for line in file:
            position = [i for i in line.split()]
            x.append(position[0])
            costs.append(position[1])
            amortized_time.append(position[2])
        
        plt.plot(x, costs, c='r', label='Cout réél')
        plt.plot(x, amortized_time, c='g', label='Cout amorti')
        plt.legend()
        saved_file =dot_file.split('.')[0]+".png"
        fig.savefig(saved_file)


