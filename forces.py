from node import Node3D,Node2D

def force_replusion(node1, node2, G=2):
    # calcule la force de replusion (acc) entre node1 et le node2
    distance = node1.distance(node2)
    acc = 0
    if distance > 0:
        acc = G*node1.masse*node2.masse/distance**2
        node1.update_velocity(node2, acc)

def force_attraction(node1, node2, G=2.0, distance_min=0.000005):
    #on calcule la force d'attraction(acc) entre le node1 et node2 à partir de cette formule
    acc = -G/node1.masse
    #on met a jour les vitesses du node1 et node2

    distance = node1.distance(node2)
    
    if distance > distance_min:
        node1.update_velocity(node2, acc)

def force_repulsion_cube(node1, cube, G=2.0):
    #ici on calcule la force de replusion(acc) entre le node1 et le centre de gravité du cube
    #on construit node2 avec la position du centre de gravité du cube
    node2 = Node3D(cube.center_point[0], cube.center_point[1], cube.center_point[2])

    #on calcule la force de replusion puis on met à jour la vitesse du node1
    distance = node1.distance(node2)
    acc = 0
    if distance > 0:
        acc = G*node1.masse*node2.masse/distance**2
        node1.velocity_x += (node1.x-node2.x)*acc
        node1.velocity_y += (node1.y-node2.y)*acc        
        node1.velocity_z += (node1.z-node2.z)*acc

def force_repulsion_rectangle(node1, rectangle, G=2):
    node2 = Node2D(rectangle.center_point[0], rectangle.center_point[1])
    distance = node1.distance(node2)
    acc = 0
    if distance > 0:
        acc = G*node1.masse*node2.masse/distance**2
        node1.velocity_x += (node1.x-node2.x)*acc
        node1.velocity_y += (node1.y-node2.y)*acc