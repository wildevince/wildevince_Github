# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:16:28 2018

@author: Chaton&Minou
"""
#pip install pypi

import sys, os, random, re 


class node : # class abstraite
    """
    niveau # position dans l'arbre
    distance # durée évolutive (en MA)
    parent # donne le noeud parent
    isRoot # logical
    list_filles # donne la liste des descendants directs
    """

class feuille (node) :
    """
    value # information philogénique
    """
    
### lecture des tree
genes = open("C:\Users\Chaton&Minou\Documents\Python_project\HMIN113\Projet_philogenie\gene_tree.nwk")
species = open("C:\Users\Chaton&Minou\Documents\Python_project\HMIN113\Projet_philogenie\species_tree.nwk")
# ca marche pas !!!!!! arg ! 

liste_genes = re.findall("'([^'(),;]+)_[^'(),;]+'")
if ( liste_genes.length == 0) : print("Erreur de capteur")
print(liste_genes)

