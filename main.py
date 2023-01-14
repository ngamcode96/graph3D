from plot3D import Plot3D
from plot2D import Plot2D
import networkx as nx

#constantes
G = 1.5
theta_max = 0.80
dt = 0.05
distance_min = 0.000005 #distance minimale entre deux noeuds voisins
n_iter = 100

#chargement du graph
Graph = nx.Graph(nx.nx_pydot.read_dot("data/benzène.dot"))
nodes = Graph.nodes()
edges = Graph.edges()

plot_3D = Plot3D(nodes, edges)

#générer des positions aléatoires pour les noeuds du graph
plot_3D.generate_random_positions_of_nodes()

#visualisation initiale:

plot_3D.plot()

#mis à jour des positions des noeuds en optimisant les calculs des forces
plot_3D.update_positions(Graph, G=G,theta_max=theta_max, dt=dt, distance_min=distance_min, n_iter=n_iter, enable_analyzer=False)

#methode naive O(n**2)
#plot_3D.update_positions_naive(Graph, G=G, dt=dt, distance_min=distance_min, n_iter=n_iter, enable_analyzer=False)


#visualisation finale*
plot_3D.plot()



###Visualisation en 2D #####

# plot_2D = Plot2D(nodes, edges)

# #générer des positions aléatoires pour les noeuds du graph
# plot_2D.generate_random_positions_of_nodes()

# #visualisation initiale:

# plot_2D.plot()

# #mis à jour des positions des noeuds
# plot_2D.update_positions(Graph, G=G,theta_max=theta_max, dt=dt, distance_min=distance_min, n_iter=n_iter, enable_analyzer=False)

# #visualisation finale*
# plot_2D.plot()


