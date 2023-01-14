import numpy as np

class Node3D:
    def __init__(self, x, y,z, masse=1):
        self.x = x
        self.y = y
        self.z = z
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.velocity_z = 0.0
        self.masse = masse
    
    def distance(self, node):
        return np.sqrt((self.x-node.x)**2 + (self.y-node.y)**2 + (self.z - node.z)**2)
    
    def update_velocity(self,node, acc):
        self.velocity_x += (self.x-node.x)*acc
        self.velocity_y += (self.y-node.y)*acc
        self.velocity_z += (self.z-node.z)*acc
        
        node.velocity_x -= (self.x-node.x)*acc
        node.velocity_y -= (self.y-node.y)*acc
        node.velocity_z -= (self.z-node.z)*acc
        
    def update_position(self, dt=0.05):
        self.x += self.velocity_x*dt
        self.y += self.velocity_y*dt        
        self.z += self.velocity_z*dt



class Node2D:
    def __init__(self, x, y, masse=1):
        self.x = x
        self.y = y
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.masse = masse
    
    def distance(self, node):
        return np.sqrt((self.x-node.x)**2 + (self.y-node.y)**2)
    
    def update_velocity(self,node, acc):
        self.velocity_x += (self.x-node.x)*acc
        self.velocity_y += (self.y-node.y)*acc
        
        node.velocity_x -= (self.x-node.x)*acc
        node.velocity_y -= (self.y-node.y)*acc
        
    def update_position(self, dt=0.05):
        self.x += self.velocity_x*dt
        self.y += self.velocity_y*dt        






