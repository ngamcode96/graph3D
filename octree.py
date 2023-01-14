#NGAM Amadou
#SARR Serigne Abdou Lat
#FALL Moussa

from node import Node3D
from forces import force_replusion, force_repulsion_cube

class Octree:
    #Octree est définit à partir d'un cuben d'une capacité, des noeuds fils(8 au total) et d'un attribut is_divided pour 
    #vérifie s'il a des sous octrees.
    def __init__(self, cube, capacity=3):
        self.cube = cube
        self.capacity = capacity
        self.nodes = []
        self.is_divided = False

    #cette methode permet d'insérer un node dans un octree  
    def insert(self, node):
        #on vérifie d'abord si un noeud ne peut pas etre contenu dans cube du self(octree)
        if self.cube.cannot_contain_node(node):
            return False
        
        #sinon il verifie s'il n'est pas plein. si oui on insert le noeud. 
        if len(self.nodes) < self.capacity:
            self.nodes.append(node)
            return True
        
        #si le octree(self) est plein alors on insert sur ces fils 
        #on doit d'abord vérifie que l'octree n'a pas de sous octrees
        if not self.is_divided:
            #si oui alors on divise le cube pour obtenir 8 nouveaux cubes 
            # et on créés 8 nouveaux octree à partir des cubes obtenus
            cubes = self.cube.divide_cube()
            self.octree1 = Octree(cubes['cube1'])
            self.octree2 = Octree(cubes['cube2'])
            self.octree3 = Octree(cubes['cube3'])
            self.octree4 = Octree(cubes['cube4'])
            self.octree5 = Octree(cubes['cube5'])
            self.octree6 = Octree(cubes['cube6'])
            self.octree7 = Octree(cubes['cube7'])
            self.octree8 = Octree(cubes['cube8'])

            self.is_divided = True

        #maintenant ici on insert le noeud sur un des octrees obtenus précédement dépendant des ses coordonnées. 
        if self.octree1.insert(node):
            return True
        elif self.octree2.insert(node):
            return True
        elif self.octree3.insert(node):
            return True
        elif self.octree4.insert(node):
            return True
        elif self.octree5.insert(node):
            return True
        elif self.octree6.insert(node):
            return True
        elif self.octree7.insert(node):
            return True
        elif self.octree8.insert(node):
            return True
        else:
            return False
        
    #force de repulsion en utilisant l'optimisation de Barnes Hut
    def force_replusion_gravity_center_3D(self, node, G=2.0, theta_max=1.2):
        #si l'octree(self) a un seul noeud alors on applique la force de replusion entre ses deux nodes directement
        if len(self.nodes) == 1:
            force_replusion(node, self.nodes[0])
        else:
            #sinon 
            #on créé un node à partir du centre de gravité
            gravity_center_node = Node3D(self.cube.center_point[0], self.cube.center_point[1], self.cube.center_point[2])
            volume = self.cube.volume()
            distance = node.distance(gravity_center_node)

            # si la distance* theta_max > volume alors on calcule la force de répulsion entre node et le centre de gravité du cube
            if distance * theta_max > volume:
                force_repulsion_cube(node, self.cube)
            else:
                #sinon on fait un appel récusive sur les octrees enfants
                if self.is_divided:
                    self.octree1.force_replusion_gravity_center_3D(node)
                    self.octree2.force_replusion_gravity_center_3D(node)
                    self.octree3.force_replusion_gravity_center_3D(node)
                    self.octree4.force_replusion_gravity_center_3D(node)
                    self.octree5.force_replusion_gravity_center_3D(node)
                    self.octree6.force_replusion_gravity_center_3D(node)
                    self.octree7.force_replusion_gravity_center_3D(node)
                    self.octree8.force_replusion_gravity_center_3D(node)
                       
            
        
        
        
        