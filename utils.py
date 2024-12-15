from dataclasses import dataclass 

import os
import urllib.request


aoc_session = os.environ.get('AOC_SESSION') 
assert aoc_session, "session cookie is missing"

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


def download_input(day, year=2024):
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cached_path = f"/tmp/aoc-{year}/{day}"
    cached = f"{cached_path}/input.txt"
    if os.path.isfile(cached):
        with open(cached) as file:
            return file.read().splitlines()
    else:
        request = urllib.request.Request(url)
        request.add_header('Cookie', aoc_session)
        with urllib.request.urlopen(request) as response:
            content = response.read().decode('utf-8')
            os.makedirs(cached_path, exist_ok=True)
            with open(cached, 'w') as file:
                file.write(content)
            return content.splitlines()
 