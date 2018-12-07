# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:16:28 2018

@author: Chaton&Minou
"""
#pip install pypi

import arbre

def gene() :
    with open("gene_tree.nwk") as g :
        sequence = g.read()  # premiere ligne du ficher
        sequence = sequence.strip("\n")
        gene = arbre.Tree(seq = sequence ) 
    g.close() # on a arbre !
    return (gene)
#list_tree = []   # créer la liste des nodes de l'arbre
    #list_gene_tree[0].isRoot()  # test qui renvoie true

def species() :
    with open("species_tree.nwk") as s:
        sequence = s.read()  # premiere ligne du ficher
        sequence = sequence.strip("\n")
        species = arbre.Tree(seq = sequence )
    s.close() # on a arbre !
    return (species)
#list_tree = []   # créer la liste des nodes de l'arbre
    #list_species_tree[0].isRoot()  # test qui renvoie true
#"""
  
def fake() :
    with open("fake_tree.nwk") as s:
        sequence = s.read()  # premiere ligne du ficher
        sequence = sequence.strip("\n")
        fake = arbre.Tree(seq = sequence )
    s.close() # on a arbre !
    return (fake)

# 
#       <Main>    <Main>    <Main>   <Main>    <Main>    <Main>   <Main>
#


retry = True
while retry :
    print("Quel arbre voulez-vous integrer ?\n 1: arbre des gènes\n 2: arbre des espèces\n 3: arbre exemple")
    ans = input()
    if ans == '1' : 
       print("Vous avez choisi l'arbre des gènes.")
       retry = False
       gene().control_tree()
       gene().parcour()
    elif ans == '2' :
        print("Vous avez choisi l'arbre des espèces.")
        retry = False
        species().control_tree()
        species().parcour()
    elif ans == '3' :
        print("Vous avez choisi le fake tree.")
        retry = False
        #fake().control_tree()
        fake().parcour()
    else : print ("Tapper 1 ou 2 \nstp !")



 
#print ("\nla liste des node de l'arbre = \n", node.afficher (list_tree) )
#print ("\nla liste des node de l'arbre = \n", node.afficher (parcour( node.fake())) )




