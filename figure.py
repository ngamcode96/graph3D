#NGAM Amadou
#SARR Serigne Abdou Lat
#FALL Moussa

import numpy as np

class Cube:
    #on definit un cube à partir de son centre de gravité et de sa longueur
    def __init__(self, center_point, length=4):
        self.center_point = center_point
        self.length = length

    #volume longueur**3 
    def volume(self):
        return self.length**3
    
    #methode qui permet de diviser un cube en 8 autres cubes
    def divide_cube(self):
        length = self.length / 2
        cubes = {
                'cube1' : Cube(np.array([self.center_point[0] - length, self.center_point[1] - length, self.center_point[2] - length]), length),
                'cube2' : Cube(np.array([self.center_point[0] - length, self.center_point[1] - length, self.center_point[2] + length]), length),
                'cube3' : Cube(np.array([self.center_point[0] - length, self.center_point[1] + length, self.center_point[2] - length]), length),
                'cube4' : Cube(np.array([self.center_point[0] - length, self.center_point[1] + length, self.center_point[2] + length]), length),
                'cube5' : Cube(np.array([self.center_point[0] + length, self.center_point[1] - length, self.center_point[2] - length]), length),
                'cube6' : Cube(np.array([self.center_point[0] + length, self.center_point[1] - length, self.center_point[2] + length]), length),
                'cube7' : Cube(np.array([self.center_point[0] + length, self.center_point[1] + length, self.center_point[2] - length]), length),
                'cube8' : Cube(np.array([self.center_point[0] + length, self.center_point[1] + length, self.center_point[2] + length]), length)
        }
        
        return cubes
    
    #methode qui vérifie si un node ne peut pas etre contenu dans un cube
    def cannot_contain_node(self, node):
        return  not (((self.center_point[0] - self.length /2) <=node.x <= (self.center_point[0] + self.length /2)) and ((self.center_point[1] - self.length /2) < node.y < (self.center_point[1] + self.length /2)) and ((self.center_point[2] - self.length /2) < node.z < (self.center_point[2] + self.length /2)))
    

        
class Rectangle:
    def __init__(self,center_point, width, height):
        self.center_point = center_point
        self.width = width
        self.height = height
        self.top = center_point[1] - height/2
        self.bottom = center_point[1] + height/2
        self.left = center_point[0] - width/2
        self.right = center_point[0] + width/2
        
    def surface(self):
        return self.height*self.width
    
    def divide_rectangle(self):
        height = self.height / 2
        width = self.width / 2
        rectangles = {
        'top_left' : Rectangle(np.array([self.center_point[0] - width/2, self.center_point[1] + height/2]), width, height),
        'top_right' : Rectangle(np.array([self.center_point[0] + width/2, self.center_point[1] + height/2]), width, height),
        'bottom_left' : Rectangle(np.array([self.center_point[0] - width/2, self.center_point[1] - height/2]), width, height),
        'bottom_right' : Rectangle(np.array([self.center_point[0] + width/2, self.center_point[1] - height/2]), width, height)
        }
        return rectangles
    

    def draw(self, ax):
        ax.plot([self.left, self.right, self.right, self.left, self.left], [self.top, self.top, self.bottom, self.bottom, self.top], c='b', lw=0.3)