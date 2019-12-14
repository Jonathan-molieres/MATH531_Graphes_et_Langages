# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:39:22 2019

@author: Simon Guilbert
"""

# =============================================================================
# Ceci est le script du TP1 mis en ligne sur l'EAD le 07/12/2019.
# La modification par rapport à la première version envoyée à la 
# fin de la séance du 28/11/2019 se situe au niveau de la méthode
# father qui ne fonctionnait pas correctement (oublie d'un argument).
# =============================================================================

# Question 1
class Node:
    # Constructeur
    def __init__(self,label,children):
        self.label = label
        self.children = children
    
    # Question 2
    def content(self):
        return self.label
    
    def children_Node(self):
        for fils in self.children:
            print(fils.label)
    


# Question 3.1
class Rtree:
    def __init__(self,racine):
        self.racine = racine
        
    def root(self):
        return self
    
    # Question 3.2
    def sub_tree(self):
        return self.racine.children
        
    # Question 3.3 
    # Méthode pour savoir si le noeud traité est une feuille
    def is_leaf(self):
        return self.sub_tree() == []
    
    # Méthode pour afficher les étiquettes de l'arborescence avec un parcours en profondeur
    def display_depth(self):
        print(self.racine.label)
        if not self.is_leaf():
            for fils in self.sub_tree() :
                Rtree(fils).display_depth()
                
    # Question 3.4
    # Méthode pour afficher les étiquettes de l'arborescence avec un parcours en largeur        
    def display_width(self):
        print(self.racine.label)
        self.__display_width()
        
    # On utilise une méthode cachée (grâce à __) pour traiter le cas particulier : afficher le label de la 1ere racine   
    def __display_width(self):
        for fils in self.sub_tree() :
            print(fils.label)
        for fils in self.sub_tree() :
            Rtree(fils).__display_width()
    
    def father(self,nodeFils):
        if not self.is_leaf():
            for fils in self.sub_tree() :
                if fils == nodeFils:
                    print(self.racine.label)
                Rtree(fils).father(nodeFils)
        
              
            
# Question 1
node6 = Node('9',[])
node5 = Node('3',[])
node4 = Node('3',[])
node3 = Node('m',[])   
node2 = Node('a',[])
node1 = Node('2',[node4,node5,node6])
node0 = Node('z',[node1,node2,node3])

# Question 3.3   
print("Question 3.3")            
Rtree(node0).display_depth() 

# Question 3.4  
print("Question 3.4")              
Rtree(node0).display_width() 

# Question 4.children.Node
print("Question 4.children_Node") 
node0.children_Node()

# Question4.father
print("Question 4.father")
Rtree(node0).father(node6)


''' Résumé de la séance :
    C'est la première fois que je code en récursif et j'ai eu beaucoup de mal à trouver une solution à partir de la question 3.4
    Je n'arrive pas à tester la méthode father car il manque un argument, mais je ne comprends pas pourquoi
'''  
