# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:27:27 2018

@author: Chaton&Minou
"""


#import sys, os, random, re 


class Node : # class abstraite
    def __init__ (self, **kwargs):
        self.name = kwargs.get('name')
        self.parent = kwargs.get('parent')
        self.enfants = kwargs.get('enfants')
        self.dist = kwargs.get('dist')
        self.gen = kwargs.get('gen')
    
    def isRoot(self):   # test 
        if self.parent:
            return (False)
        else:
            return (True)
    
    def isLeaf(self):  # test
        if self.enfants:
            return (False)
        else:
            return (True)
        
    def __repr__(self):
                return("nom({}) generation({}) enfants({})".format
                (self.name, self.gen, self.enfants,))

# fin class 



