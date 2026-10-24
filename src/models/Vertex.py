from dataclasses import dataclass, field

@dataclass

class Vertex:
    tag: str
    links: dict = field(default_factory=dict)
    value: any
    visited: bool
