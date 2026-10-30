from dataclasses import dataclass, field

@dataclass

class Vertex:
    tag: str
    links: dict = field(default_factory=dict)
    value: any = None
    visited: bool=False
    
    def add_link(self,destiny, weigth):
        
        currenly_weigth=[]
        
        if(destiny in self.links):
            currenly_weigth=self.links[destiny]
        
        currenly_weigth.append(weigth)
        
        self.links[destiny]=currenly_weigth
    
    def mark_as_visited(self):
        self.visited=True
        
    def get_links(self):
        return self.links
    
    def lower_cost_link(self,visited=None):
        
        if visited is None:
            visited=[]
        
        lower=None
        lower_destiny=None
        for destiny,cost in self.links.items():
            
            if destiny in visited:
                continue
            
            for c in cost:
                if lower is None or c<lower:
                    lower=c
                    lower_destiny= destiny
        
        
                    
        lower_link=(self.tag,lower_destiny,lower) 
            
        return lower_link
    
    
    
    
        
        
