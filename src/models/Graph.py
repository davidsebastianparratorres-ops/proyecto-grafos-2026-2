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
            
            
            
                            
            
        
        
        
        
       
       