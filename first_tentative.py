# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:16:28 2018

@author: Chaton&Minou
"""
#pip install pypi

import sys, os, random, re 


class node : # class abstraite
    def __init__ (self, **kwargs):
        self.name = kwargs.get('name')
        self.parent = kwargs.get('parent')
        self.enfants = kwargs.get('enfants')
        self.gen = kwargs.get('gen')
    
    def isRoot():   # test 
        if self.parent:
            return false
        else:
            return true
    def isLeaf():  # test
        if self.enfants:
            return false
        else:
            return true
# fin class    
    """
    niveau # position dans l'arbre
    distance # durée évolutive (en MA)
    parent # donne le noeud parent
    isRoot # logical
    list_filles # donne la liste des descendants directs
    
class feuille (node) :
    
    value # information philogénique
"""
    
### lecture des tree
#genes = open("C:\Users\Chaton&Minou\Documents\Python_project\HMIN113\Projet_philogenie\gene_tree.nwk")
#species = open("C:\Users\Chaton&Minou\Documents\Python_project\HMIN113\Projet_philogenie\species_tree.nwk")
# ca marche pas !!!!!! arg ! 


"""
with open("gene_tree.nwk") as g:
    arbre = g.read()  # premiere ligne du ficher
g.close() # on a arbre !
#list_tree = []   # créer la liste des nodes de l'arbre
    #list_gene_tree[0].isRoot()  # test qui renvoie true
    
"""
def gene() :
    with open("gene_tree.nwk") as g:
        arbre = g.read()  # premiere ligne du ficher
        arbre = arbre.strip("\n")
    g.close() # on a arbre !
    return (arbre)
#list_tree = []   # créer la liste des nodes de l'arbre
    #list_gene_tree[0].isRoot()  # test qui renvoie true

def species() :
    with open("species_tree.nwk") as s:
        arbre = s.read()  # premiere ligne du ficher
        arbre = arbre.strip("\n")
    s.close() # on a arbre !
    return (arbre)
#list_tree = []   # créer la liste des nodes de l'arbre
    #list_species_tree[0].isRoot()  # test qui renvoie true
#"""
  
    
def control_tree(arbre) :
    print("premier caractère = ", arbre[0])
    print("dernier caractére = ", arbre[len(arbre) -1] )
    print("longueur de l'arbre = " , len(arbre))
# fin 

def parcour (arbre, niveau = 0, index = 1) :  # commencer à la fin "
    # niveau = niveau de l'arbre
    # index = l'indice de la lettre suivante
    list_node = [] 
    i = (len(arbre) - index)  # on demarre au dernier caractere 
    while ( i >= 0) :
    #for i in arbre :
        #compteur += 1
        if (arbre[i] == ';') :  # C le root !
            list_node.append(node(gen = niveau, enfant = parcour(arbre, niveau +1, index +1)))
            
        elif (arbre[i] == ')' )  : # entre dans une feuillle
                #niveau += 1   # local variable qui descrit : self.gen 
            list_node.append(node(gen = niveau, enfant = parcour(arbre, niveau + 1, index +1)))
            
        elif (arbre[i] == ',' ) : # création d'un "frére" : feuille orthologue
            list_node.append(node(gen = niveau))
            
        elif (arbre[i] == '(' ) : # fermer le node : relation parent/enfants
            return ("Zone en travaux : Veuillez revenir plutard !")
        else : # valeur ou longueur : "I know RegEx"
            continue
            #return ("Zone en travaux : Ne revenez jamais !")
        i -= 1 #decrementation du while
    #list_tree = list_tree.extend(list_node) 
    return (list_node )
# .
#print ("\nlist_node = \n", list_node)

retry = True
while retry :
    print("Quel arbre voulez-vous integrer ?\n 1: arbre des gènes\n 2: arbre des espèces")
    ans = input()
    if ans == '1' : 
        print("Vous avez choisi l'arbre des gènes.")
        retry = False
        control_tree(gene())
        print ("\nla liste des node de l'arbre = \n",  parcour(gene()) )
    elif ans == '2' :
        print("Vous avez choisi l'arbre des espèces.")
        retry = False
        control_tree(species())
        print ("\nla liste des node de l'arbre = \n",  parcour(species()) )
    else : print ("Tapper 1 ou 2 \nstp !")
# .





"""
list_genes = re.findall("'([^'(),;]+)_([^'(),;]+)'")  
# j'extrait tous les nom scient (group 1) et les genes (group 2)
if ( liste_genes.length == 0) : print("Erreur de capture")
print(liste_genes)
"""
#list_species = re.findall("'([^'(),;]+)'")


