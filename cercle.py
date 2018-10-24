#! /usr/bin/python3

from chord import Noeud

class Cercle:
	
	def __init__(self,nbNode):
		
		self.nbNode = nbNode
	
	def creerCercle(self):
		
		ip ="127.0.0.1"
		for n,node in enumerate(range(0, self.nbNode)):
			 self.nodes.append(Node(ip, int(n))
			 
		for node in self.nodes:
            if node is not self.nodes[0]:
                self.nodes[0].addToCircle(node)
        
        return self.nodes
			 

