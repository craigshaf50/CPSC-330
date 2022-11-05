# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:52:47 2021

@author: swamy
"""

class Vertex:
    def __init__(self,key):
        self.id = key
        self.color = 'white'
        self.connectedTo = {}
        self.discovery = 0
        self.finish = 0
        self.pred = None
    
    def setPred(self, v):
       self.pred = v
   
    def getPred(self):
       return self.pred
    
    def setColor(self, c):
        self.color = c
   
    def setDiscovery(self, t):
        self.discovery = t
   
    def getDiscovery(self):
        return self.discovery
        
    def setFinish(self, t):
        self.finish = t
    
    def getFinish(self):
        return self.finish
     
    def getColor(self):
        return self.color
     
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]