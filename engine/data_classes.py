from dataclasses import dataclass, field

@dataclass
class Pac_Man:
    x: int
    y: int
    score: int
    lives: int
    current_step: str
    is_dead: bool
    spawn_position: tuple[int]

    def respawn(self):
        self.y, self.x = self.spawn_position

    def put_new_coordinates(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return "Pac-Man"

    def __repr__(self):
        return"C"

@dataclass
class Ghost:
    color: str
    x: int
    y: int
    is_dead: bool
    spawn_position: tuple[int]

    def respawn(self):
        self.y, self.x = self.spawn_position

    def put_new_coordinates(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.color[0] + "  "