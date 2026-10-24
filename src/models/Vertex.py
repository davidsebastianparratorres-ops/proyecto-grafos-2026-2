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
    
    
    
        
        
