# -*- coding: utf-8 -*-

"""
Created on Wed Nov 28 15:27:27 2018

@author: Chaton&Minou
"""


#import sys, os, random, re 
import node



def last_index( liste ) :
    nbr = 0
    for k in liste :
        nbr += 1
    return (nbr-1)
# fin 

def last_kids( liste, nbr ) :
    kids = []
    while nbr > 0 :
        kids.append( last_index(liste) )
        del liste [-1]
        nbr -= 1 
    return kids
# fin  



class Tree : 
    def __init__ (self, **kwargs):
        self.list_tree = kwargs.get('list_tree') # liste de node
        self.arbre =  kwargs.get('seq') # la sequence newick
        self.tools = kwargs.get('tools')

    def control_tree(self) :
        print("\npremier caractère : %s " %( self.arbre[0] ))
        print("dernier caractére = %s" %( self.arbre[ len( self.arbre) -1] ))
        print("longueur de l'arbre = %s\n" %(len( self.arbre )))

    def re_tools( self , i = False ) :
        self.tools = {} 
        self.tools["i"] = i
        self.tools["j"] = 1
        self.tools["valeur"] = ""
        self.tools["nom"] = ""
# fin

    def recup(self ) :
        # self = arbre
        self.re_tools( self.tools["i"] )
        ### Bloc recup valeur !!!
        while ( self.arbre[ self.tools["i"] - self.tools["j"] ] != ")" 
              and self.arbre[ self.tools["i"] - self.tools["j"] ] != "," 
              and self.arbre[ self.tools["i"] - self.tools["j"] ] != "(" ) :  
            # si la prochaine lettre est une value
            #self.touch()
            #print("j + 1 ? \t(y/n)")
            #if ( input() == 'n' ) : print("erreur sur recup() ")
            #
            if( self.arbre[ self.tools["i"] - self.tools["j"] ] == ':'): # démarque par la distance puis par le nom
                self.tools["j"] -= 1
                while( self.tools["j"] > 0): 
                    self.tools["valeur"] += self.arbre[ self.tools["i"] - self.tools["j"] ]  # on récuper le mot
                    self.tools["j"] -= 1
                self.tools["i"] -= self.tools["j"]            # réinitialisation
                self.tools["j"] = 1
            else : self.tools["j"] += 1       # alors on se met à son niveau
        self.tools["j"] -= 1
        while( self.tools["j"] > 0): 
            self.tools["nom"] += self.arbre[ self.tools["i"] - self.tools["j"] ]  # on récuper le mot   
            self.tools["j"] -= 1
        #on rattrape juste apres les valeurs
        self.tools["i"] -= self.tools["j"]            # réinitialisation
        self.tools["j"] = 1 
        #print("fin de récup() ")
        ### on a récupere la distance du node et le nom du node , s'il y a !
# fin

    def afficher( self ) :
        print ("Liste des %s node : " %( len(self.list_tree) ))
        for n in self.list_tree : 
            print("[nom = {} ; distance = {} ; niveau = {} ]" .format(n.name, n.dist, n.gen) )
                      
# fin def


    def parcour ( self , niveau = 0 ) :  # commencer à la fin "
        # niveau = niveau de l'arbre
        self.re_tools( (len(self.arbre) - 1) ) 
        # on demarre au dernier caractere 
        index_parent = []  # contient les index des parents
        index_enfants = []  # contient les index des enfants/(niveau du parent associé)
        self.list_tree = []
        self.enfants = []
        #
        while ( self.tools["i"] >= 0) :  # i compte le nbre de lettre qu'il reste à parcourir
            # controle de l'avancement 
            self.re_tools( self.tools["i"] ) 
            #
            """
            print ("\t re_tools\n controle indice = %s" %( self.tools["i"] ) )
            print ("Controle lettre = %s" %( self.arbre[ self.tools["i"] ] ))
            print ("Controle j = %s" %( self.tools["j"] ))
            print ("Controle distance = %s" %( self.tools["valeur"] ))
            print ("Controle nom du node = %s \n" %( self.tools["nom"] ))
            """
            # à chaque lettre on réinitialise les variables
            #
            # case loop !
            if (self.arbre[ self.tools["i"] ] == ';') :  # C le root !
                #print("C'est le pied !\t Création du root !!!")
                self.recup() 
                self.list_tree.append( node.Node(gen = niveau, dist = self.tools["valeur"], name = "root" ))
                
                
            elif (self.arbre[ self.tools["i"] ] == ')' )  : # entre dans une feuillle
                #print("nouvelle feuille")
                index_enfants.append( niveau )
                index_enfants[niveau] = []
                niveau += 1
                #print(niveau)
                index_parent.append( last_index(self.list_tree) )
                #print(index_parent)
                self.recup()  
                self.list_tree.append( node.Node(gen = niveau, dist = self.tools["valeur"], name = self.tools["nom"]) )
                index_enfants[niveau-1].append( last_index(self.list_tree) )
                            
            elif (self.arbre[ self.tools["i"] ] == ',' ) : # création d'un "frére" : feuille orthologue
                #print("orthologue")
                self.recup() 
                self.list_tree.append( node.Node(gen = niveau, dist = self.tools["valeur"], name = self.tools["nom"]) )
                index_enfants[niveau-1].append( last_index(self.list_tree) )
                
            elif (self.arbre[ self.tools["i"] ] == '(' ) : # fermer le node : relation parent/enfants
                #print("fermeture du noeud")
                # ajoute au dernier parent la liste des enfants du bon niveau
                # ensuite on supprime le dernier parent !
                niveau -= 1
                self.list_tree[ last_index(index_parent) ].enfants = index_enfants[niveau]
                #print("controle liste enfant du dernier parent = %s" 
                #      % ( self.list_tree[ last_index(index_parent) ].enfants ))
                del index_parent[-1]
            self.tools["i"] -= 1 #decrementation du while
            #self.touch()
            #
            """
            print ("\nControle j = %s" %( self.tools["j"] ))
            print ("Controle distance = %s" %( self.tools["valeur"] ))
            print ("Controle nom du node = %s" %( self.tools["nom"] ))
            print ("Controle liste de node = %s" %( self.list_tree ))
            print ("Controle niveau %s" %( niveau ))
            print ("Controle parent = %s" %( index_parent ))
            print ("Controle enfants = %s" %( index_enfants ))
            """
            #print("\n next ? \t(y/n)")
            #if ( input() == 'n' ) : return ( self.afficher() )
        return ( self.afficher() )
    
    def touch(self) :
        print( self.arbre )
        truc = ""
        trucc = ""
        k = 0
        while k < len(self.arbre) :
            if k == self.tools['i'] : truc += 'i'
            else : truc += ' '
            if k == (self.tools['i'] - self.tools['j']) : trucc += 'j'
            else : trucc += ' '
            k += 1
        print(truc)
        print(trucc)
        #
        

# fin class
    
