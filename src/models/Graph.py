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
        
        
                
                
          
        
        """ 
        stack=deque()
        recorrido=[]
        initial_node=self.vertex[tag]   
        stack.append(initial_node)
        initial_node.mark_as_visited()
        currenly_node=initial_node
        recorrido.append(initial_node.tag)
        
        
        
        while len(stack)>0:
            
            next_node=next((currenly_node.links[tag] for tag in currenly_node.links if not currenly_node.links[tag].visited),None)
            
            if next_node is not None:
                stack.append(next_node)
                next_node.mark_as_visited()
                currenly_node=next_node
                recorrido.append(currenly_node.tag)
                
            else:
                stack.pop()
                if len(stack) > 0:
                    currenly_node=stack[-1]
    
        return recorrido 
        """
    
    def least_expensive_link(self):
        
        for tag, value in self.vertex.items():
            for cost in value.links:
                return    
                
                

    
            
            
            
                            
            
        
        
        
        
       
       