# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 07:48:05 2019

@author: Jonathan Molières et Simon Guilbert
"""

class Etape:
     # Constructeur 
    def __init__(self,number,AuPlusTot,AuPlusTard,taches):
        
        self.number = number       
        self.AuPlusTot = AuPlusTot
        self.AuPlusTard = AuPlusTard
        self.taches = taches
        '''
         Le parametre taches contient la liste des etapes filles du noeud. Il sera initialise a la main en tant que liste vide à cause 
         d'un bug de Spyder qui garde la même liste pour toutes les étapes creees (vu avec M.Mauffret) : quand on ajoute la tâche à la liste (= taches) de 
         l'objet Etape correspondant au begin_step de l'objet Tache associé, cette liste n'est jamais réinitialisée, alors qu'elle le devrait étant donné 
         que chaque objet Etape contient sa propre liste.
        '''    
    def get_au_plus_tot(self) :
        return self.AuPlusTot
    
    def get_au_plus_tard(self) :
        return self.AuPlusTard
    
    def get_number(self) :
        return self.number
    
    def get_taches(self):
        return self.taches
    
    def get_next_steps(self) :
        L=[]
        for tache in self.taches:
            L.append(tache.get_end_step())
        return L
    
    def get_previous_steps(self,etape) :
        if self==etape:
            return self
        for noeud in self.get_next_steps():
            if noeud==etape:
                print( self.number)
                
            noeud.get_previous_steps(etape)
            
    
   
class Tache:
    # Constructeur
    def __init__(self,name,duration,begin_step,end_step):
        
        self.name=name
        self.duration=duration
        self.begin_step = begin_step
        self.end_step = end_step
        self.begin_step.taches.append(self)
           
    def get_name(self) :
        return self.name
    
    def get_duration(self) :
        return self.temps
    
    def get_begin_step(self) :
        return self.begin_step
    
    def get_end_step(self) :
        return self.end_step



class Pert:
      def __init__(self,racine):  
          self.racine=racine
          
      def critique(self) :
          # affiche les etapes critiques
        print(self.racine.number)
        for noeud in self.racine.get_next_steps():
            if noeud.get_au_plus_tot()==noeud.get_au_plus_tard():
                Pert(noeud).critique()
                             
      def compte_au_plus_tot(self):
#        Permet d'affecter la date au plus tot si elle n'est pas definie en partant de la condition que la 
#        premiere etape est initialisée
        
        for i in range(len(self.racine.get_next_steps())):
            if self.racine.get_next_steps()[i].AuPlusTot < self.racine.AuPlusTot+self.racine.taches[i].duration:
                self.racine.get_next_steps()[i].AuPlusTot=self.racine.AuPlusTot+self.racine.taches[i].duration
            Pert(self.racine.get_next_steps()[i]).compte_au_plus_tot()
        
        def dernier(self):
            #permet d'obtenir la derniere etape dont la date au plus tard est connue
            for noeud in self.racine.get_next_steps():
                if noeud.get_next_steps()==[]:
                    noeud.AuPlusTard=noeud.AuPlusTot
                Pert(noeud).dernier()
           
        def compte_au_plus_tard(self):
            #fonctionne comme compte_au_plus_tot en partant par la derniere etape
            pass
        

# =============================================================================
# Question 1 : Creation des Etapes et taches
# =============================================================================        
# Permet d'implementer le DAG defini par le TP
          
e8=Etape(8,220,220,[])
e7=Etape(7,210,210,[])
e6=Etape(6,150,150,[])
e5=Etape(5,50,210,[])
e4=Etape(4,40,200,[])
e3=Etape(3,150,210,[])
e2=Etape(2,120,120,[])
e1=Etape(1,30,30,[])
e0=Etape(0,0,0,[])

t1=Tache('A',30,e0,e1)
t2=Tache('B',90,e1,e2)
t3=Tache('c',30,e2,e3)
t4=Tache('D',10,e1,e4)
t5=Tache('E',10,e4,e5)
t6=Tache('ta',0,e5,e7)
t7=Tache('tb',0,e3,e7)
t8=Tache('H',10,e7,e8)   
t9=Tache('G',60,e6,e7)       
t10=Tache('F',30,e2,e6)

# =============================================================================
# Question 2
# =============================================================================
print("\nQuestion 2 : test get_next_steps")
for i in e1.get_next_steps() :
    print(i.number)

print("\nQuestion 2 : test get_previous_steps")
e0.get_previous_steps(e4)

# =============================================================================
# Question 3
# =============================================================================
print("\nQuestion 3 : etapes critiques")
# Création du diagramme de PERT ayant comme noeud racine le noeud d'étiquette "0"
P=Pert(e0)
# Calcul du chemin critique
P.critique()

# =============================================================================
# Question 4
# =============================================================================
print("\nQuestion 4")            
# Création des étapes mais sans connaître les dates au plus tot et au plus tard :
# les dates sont initialisées à 0          
e8=Etape(8,0,0,[])
e7=Etape(7,0,0,[])
e6=Etape(6,0,0,[])
e5=Etape(5,0,0,[])
e4=Etape(4,0,0,[])
e3=Etape(3,0,0,[])
e2=Etape(2,0,0,[])
e1=Etape(1,0,0,[])
e0=Etape(0,0,0,[])

t1=Tache('A',30,e0,e1)
t2=Tache('B',90,e1,e2)
t3=Tache('c',30,e2,e3)
t4=Tache('D',10,e1,e4)
t5=Tache('E',10,e4,e5)
t6=Tache('ta',0,e5,e7)
t7=Tache('tb',0,e3,e7)
t8=Tache('H',10,e7,e8)   
t9=Tache('G',60,e6,e7)       
t10=Tache('F',30,e2,e6)

# Création du diagramme de PERT sans connaître les dates de début et de fin
P1=Pert(e0)

# Calcule les dates au plus tot et au plus tard de chaque étape
P1.compte_au_plus_tot()

print(e8.AuPlusTot)
    
"""
Ressenti du TP:
Nous avons réussi à faire toutes les question sauf la dernière compteur_au_plus_tard que nous
n'avons pas eu le temps de finir. Nous avons passé du temps au début de la séance pour régler
le problème expliqué à la ligne 17 , et on ne connaît 
d'ailleurs toujours pas la raison de ce bug.
   
    
""" 

