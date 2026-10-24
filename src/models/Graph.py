from dataclasses import dataclass, field
from src.models.Vertex import Vertex
from collections import deque

@dataclass

class Graph:
    vertex:dict[str,Vertex] = field(default_factory=dict)

    def get_Vertex(self):
        return self.vertex
    
    def add_Vertex(self,tag):
        v=Vertex(tag)
        self.vertex[tag]=v
        
    def bfs(self, tag: str):
        
        if tag not in self.vertex:
            print("el vertice no se encuentra en el grafo")
            return
        
        cola=deque()
        recorrido=[]
        initial_nodo=self.vertex[tag]
        cola.append(initial_nodo)
        initial_nodo.mark_as_visited()
                
        while len(cola)>0:
            
            currenly_node:Vertex=cola.popleft()
            recorrido.append(currenly_node.tag)  
            
            
            for value in currenly_node.links:
                if not currenly_node.links[value].visited:
                    cola.append(currenly_node.links[value])
                    currenly_node.links[value].mark_as_visited()
                    
    
        return recorrido
                    
            
        
        
        
        
       
       