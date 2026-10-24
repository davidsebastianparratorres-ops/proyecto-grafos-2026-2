from dataclasses import dataclass, field
from Vertex import Vertex

@dataclass

class Graph:
    vertex:dict[str,Vertex] = field(default_factory=dict)