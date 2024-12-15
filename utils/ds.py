from dataclasses import dataclass 


@dataclass 
class p2d: 
    x: int 
    y: int 

    def __add__(self, other):
        return p2d(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self    

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

@dataclass 
class p3d: 
    x: int 
    y: int 
    z: int 

    def __add__(self, other):
        return p3d(self.x + other.x, self.y + other.y, self.z)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self    

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

