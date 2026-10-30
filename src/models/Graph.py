from dataclasses import dataclass, field
from src.models.Vertex import Vertex
from collections import deque

@dataclass

class Graph:
    vertex:dict = field(default_factory=dict)

    def get_Vertex(self):
        return self.vertex
    
    def add_Vertex(self,tag):
        v=Vertex(tag)
        self.vertex[tag]=v  
        
    def del_Vertex(self,tag):
        
        if tag not in self.vertex:
            print("No existe ese vertice en el grafo")
            return
        
        for v_tag, vertex_obj in self.vertex.items(): #se recorre cada vertice
            if tag in vertex_obj.get_links(): #si en sus enlaces esta el tag se elimina de los enlaces
                del vertex_obj.get_links()[tag]
                
        del self.vertex[tag] #se elimina el vertice del grafo
            
            
    def bfs(self, tag: str):
        
        if tag not in self.vertex:
            print("el vertice no se encuentra en el grafo")
            return
        
        dequeR=deque()
        recorrido=[]
        initial_node=self.vertex[tag]
        dequeR.append(initial_node)
        initial_node.mark_as_visited()
                
        while len(dequeR)>0:
            
            currenly_node:Vertex=dequeR.popleft()
            recorrido.append(currenly_node.tag)  
            
            
            for value in currenly_node.links:
                if not currenly_node.links[value].visited:
                    dequeR.append(currenly_node.links[value])
                    currenly_node.links[value].mark_as_visited()
                    
    
        return recorrido
    
    def dfs(self, tag: str):
        
        if tag not in self.vertex:
            print("el vertice no se encuentra en el grafo")
            return
        
        recorrido=[]
        initial_node=self.vertex[tag] 
        
        self._dfs(initial_node, recorrido)
        return recorrido
    
    def _dfs(self, currenly_node, recorrido):
        
        currenly_node.mark_as_visited()
        recorrido.append(currenly_node.tag)
        
        for neighbor_tag in currenly_node.links:
            
            neighbor_node =self.vertex[neighbor_tag]
                            
            if not neighbor_node.visited:
                self._dfs(neighbor_node, recorrido)
        
    
    def least_expensive_link(self):
        lower=None
        for value in self.vertex.values():
            if value.lower_cost_link()[2] is not None: #si el costo de la menor arista no es None  
                if lower is None or value.lower_cost_link()[2]<lower[2] :
                    lower=value.lower_cost_link()
        
        return lower
    
    def mst_prim(self):
        
        if not self.vertex:return None
        
        start=self.least_expensive_link() #(tag_origen, tag_destino, costo), empieza por el menor enlace global
        if start is None: return None
        visited=[]#lista de strings(etiquetas)
        visited.append(start[0])
        visited.append(start[1])
        mst=[]#lista de aristas(tuplas)
        mst.append(start)
        
        while(len(visited)<len(self.vertex)):#acaba cuando se visitaron todos los vertices
            
            lower=None
            
            for tag in visited:
                candidate=self.vertex[tag].lower_cost_link(visited)
                
                if candidate[2] is not None:
                    if lower is None or candidate[2]<lower[2]:
                        lower=candidate
            
            if lower is None: return None
            visited.append(lower[1])
            mst.append(lower)
        
        return mst    
            
                
                

    
            
            
            
                            
            
        
        
        
        
       
       