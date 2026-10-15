from dataclasses import dataclass

@dataclass
class Pac_Man:
    x: int = 0
    y: int = 0
    score: int = 0
    lives: int = 3
    current_step: str = ""
    is_dead: bool = False
    spawn_position: tuple[int] = (0, 0)

    def respawn(self):
        self.spawn_position = (self.y, self.x)

    def put_new_coordinates(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return "Pac-Man"

    def __repr__(self):
        return"C" + "  "

@dataclass
class Ghost:
    color: str
    x: int = 0
    y: int = 0
    is_dead: bool = False
    spawn_position: tuple[int] = (0, 0)

    def respawn(self):
        self.spawn_position = (self.y, self.x)

    def put_new_coordinates(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return self.color

    def __repr__(self):
        return self.color[0] + "  "