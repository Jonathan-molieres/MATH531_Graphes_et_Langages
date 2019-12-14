# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:12:48 2019

@author: Simon Guilbert
"""

class Node :
     # Constructeur
    def __init__(self,label,filsG = None,filsD = None):
        self.label = label
        self.filsG = filsG
        self.filsD = filsD
    
    def getValeur(self) :
        return self.label
    
    def getFils(self):
        return [self.filsG,self.filsD]
        


class ABR:
    # Constructeur
    def __init__(self,racine):
        self.racine = racine
        
    # Méthode pour obtenir la liste [filsGauche,filsDroit] d'un noeud
    def sub_tree(self):
        return self.racine.getFils()

    # Méthode pour savoir si le noeud traité est une feuille
    def is_leaf(self):
        return self.racine.filsG == None and self.racine.filsD == None
    
    def existe(self,valeur,compteur = 0) :
        compteur += 1
        if valeur < self.racine.getValeur() :
            # S'il n'existe pas de fils gauche alors il n'existe pas l'élément cherché
            if self.racine.filsG == None:
                return [False,compteur]
            # Sinon on lance la récursivité
            else :
                return ABR(self.racine.filsG).existe(valeur,compteur)
        elif valeur > self.racine.getValeur() :
            if self.racine.filsD == None:
                return [False,compteur]
            else :
                return ABR(self.racine.filsD).existe(valeur,compteur)
        else :
            # Sinon c'est que la valeur cherchée est egale à celle du noeud en cours de traitement
            return [True, compteur]
        
    # Méthode pour obtenir la liste des noeuds d'un ABR    
    def listeNoeuds(self,l=[]):
        l.append(self.racine.getValeur())
        if not self.is_leaf():
            for fils in self.sub_tree() :
                if fils != None: 
                    ABR(fils).listeNoeuds()
        return(l)
    
    # Méthode permettant d'ajouter un noeud à un ABR    
    def add_node(self,etiquette):
        if self.existe(etiquette)[0] :
            print("Erreur :",etiquette,"existe déjà")
            return "erreur"
        elif etiquette < self.racine.getValeur():
            if self.racine.filsG == None :
                self.racine.filsG = Node(etiquette)
                print("Le noeud", etiquette, 
                      "a bien été ajouté en tant que fils gauche de",
                      self.racine.getValeur())
            else :
                ABR(self.racine.filsG).add_node(etiquette)
        else :
            if self.racine.filsD == None :
                self.racine.filsD = Node(etiquette)
                print("Le noeud", etiquette, 
                      "a bien été ajouté en tant que fils droit de",
                      self.racine.getValeur())
            else :
                ABR(self.racine.filsD).add_node(etiquette)
                

class question5 :
    def __init__(self,listeNoeuds):
        # Le noeud racine de l'ABR est le noeud au milieu de la liste triée
        self.racine = ABR(Node(sorted(listeNoeuds)[len(listeNoeuds)//2]))
        for i in sorted(listeNoeuds) :
            self.racine.add_node(i)
    
    
        


# Fonction pour trouver un élément dans une liste (question 3)
def existe(liste,valeur,compteur = 0):
    for i in liste :
        compteur += 1
        if i == valeur :
            return [True,compteur]
    return [False,compteur]


# =============================================================================
# Question 2
# =============================================================================

node7 = Node(6)
node6 = Node(9)
node5 = Node(7,node7)
node4 = Node(8,node5,node6)
node3 = Node(4)
node2 = Node(1)
node1 = Node(2,node2,node3)
node0 = Node(5,node1,node4)  

# Création de l'arbre dont la racine est le noeud portant l'étiquette "5"
arbre = ABR(node0)

# =============================================================================
# Question 3
# =============================================================================
print("\nQuestion 3 avec l'arbre")
print(arbre.existe(valeur = 6))
print("\nQuestion 3 avec la liste")
liste = [1,2,4,5,6,7,8,9]
print(existe(liste, valeur = 6))

# =============================================================================
# Question 4
# =============================================================================
print("\nQuestion 4 avec l'arbre")
# Pour connaitre tous les noeuds de l'arbre
l = arbre.listeNoeuds()

# Calcul de la moyenne d'étapes necessaires pour trouver chaque noeud de l'arbre
compteurTotal = 0
for noeud in l :
    result = arbre.existe(valeur = noeud)
    compteurTotal += result[1]    
print("La moyenne est de",compteurTotal/len(l),"étapes pour trouver un noeud")

print("\nQuestion 4 avec la liste")
# Calcul de la moyenne d'étapes necessaires pour trouver chaque valeur de la liste
compteurTotal = 0
for valeur in liste :
    result = existe(liste,valeur = valeur)
    compteurTotal += result[1]    
print("La moyenne est de",compteurTotal/len(liste),"étapes pour trouver une valeur")

# =============================================================================
# Question 6
# =============================================================================
print("\nQuestion 6 : ajout du noeud 10")
arbre.add_node(10)

print("\nQuestion 6 : ajout du noeud 3")
arbre.add_node(3)

print("\nQuestion 6 : tentative d'ajout du noeud 3")
arbre.add_node(3)

# =============================================================================
# Question 5
# =============================================================================
print("\nQuestion 5")
arbre2 = question5(listeNoeuds = [1,2,4,5,6,7,8,9])



''' Résumé de la séance :
    Je pense que je me suis amélioré par rapport à la séance précédente. J'ai 
    passé du temps pour la methode existe car on ne peut pas comparer un entier 
    avec un None.
    Pour la question 4, j'ai fait à chaque fois une moyenne avec les 8 noeuds
    de l'arbre et les 8 valeurs de la liste.
    Je ne suis pas sûr d'avoir compris la question 5.
'''
