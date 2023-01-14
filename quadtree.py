from forces import *
from node import Node2D
class Quadtree:
    def __init__(self, rectangle,capacity=3):
        self.capacity = capacity
        self.rectangle = rectangle
        self.nodes = []
        self.is_divided = False
        
    def insert(self, node):
        if  not (((self.rectangle.center_point[0] - self.rectangle.width /2) <=node.x <= (self.rectangle.center_point[0] + self.rectangle.width /2)) and ((self.rectangle.center_point[1] - self.rectangle.height /2) < node.y < (self.rectangle.center_point[1] + self.rectangle.height /2))):
            return False
        
        if (len(self.nodes)) < self.capacity:
            self.nodes.append(node)
            return True
        
        if not self.is_divided:
            rectangles = self.rectangle.divide_rectangle()
            self.top_left = Quadtree(rectangles['top_left'])
            self.top_right = Quadtree(rectangles['top_right'])
            self.bottom_left = Quadtree(rectangles['bottom_left'])
            self.bottom_right = Quadtree(rectangles['bottom_right'])
            self.is_divided = True
        
        if self.top_left.insert(node):
            return True
        elif self.top_right.insert(node):
            return True
        elif self.bottom_left.insert(node):
            return True
        elif self.bottom_right.insert(node):
            return True
        else:
            return False
        

    
    def force_replusion_gravity_center_2D(self, node, G=2.0, theta_max=1.2):
        if len(self.nodes) == 1:
            force_replusion(node, self.nodes[0])
        else:
            gravity_center_node = Node2D(self.rectangle.center_point[0], self.rectangle.center_point[1])
            surface = self.rectangle.surface()
            distance = node.distance(gravity_center_node)
            
            if distance * theta_max > surface:
                force_repulsion_rectangle(node, self.rectangle)
            else:
                if self.is_divided:
                    self.top_left.force_replusion_gravity_center_2D(node)
                    self.top_right.force_replusion_gravity_center_2D(node)
                    self.bottom_left.force_replusion_gravity_center_2D(node)
                    self.bottom_right.force_replusion_gravity_center_2D(node)
    
    def draw_qt(self, ax):
        self.rectangle.draw(ax)
        if self.is_divided:
            self.top_left.draw_qt(ax)
            self.top_right.draw_qt(ax)
            self.bottom_left.draw_qt(ax)
            self.bottom_right.draw_qt(ax)
        
        for node in self.nodes:
            ax.scatter(node.x, node.y, c='red', s=10)
                    
            
            