from mazegenerator import MazeGenerator
from .data_classes import Ghost, Pac_Man

class MapGenerator:
    def __init__(
            self, width, height
            ) -> None:

        self.width = width
        self.height = height

        self.maze = MazeGenerator(size=(width, height)).maze

        self.map = self.generate_map()

    @staticmethod
    def open_cells(maze, neighbors, y, x) -> None:
        for dir in neighbors:
            match dir:
                case "N":
                    maze[y * 2][x * 2 + 1] = " "
                case "E":
                    maze[y * 2 + 1][x * 2 + 2] = " "
                case "S":
                    maze[y * 2 + 2][x * 2 + 1] = " "
                case "W":
                    maze[y * 2 + 1][x * 2] = " "

    @staticmethod
    def convert_base(number) -> str:
        base = "01"

        result = ""
        len_base = 2

        while number > 0:
            index: int = number % len_base
            result = base[index] + result
            number = number // len_base

        add_n = 4 - len(result)
        result = "0" * add_n + result
        return result


    @staticmethod
    def get_neighbors(number) -> list[str]:
        binary_n = MapGenerator.convert_base(number)
        directions = ["W", "S", "E", "N"]
        neighbors = []
        for i, c in enumerate(binary_n):
            if c == "0":
                neighbors.append(directions[i])

        return neighbors

    @staticmethod
    def closed_place(map, y, x) -> None:
        if map[y + 1][x] != "#":
            return False
        if map[y][x + 1] != "#":
            return False
        if map[y - 1][x] != "#":
            return False
        if map[y][x - 1] != "#":
            return False
        return True

    def add_ft(self, map) -> None:
        i = 0
        j = 0
        while i < self.height:
            y = i * 2 + 1 
            j = 0
            while j < self.width:
                x = j * 2 + 1
                if self.closed_place(map, y, x):
                    map[y][x] = "@"
                j += 1
            i += 1

    def pac_man_place(self, map) -> None:
        y = (self.height * 2 + 1) // 2
        x = (self.width * 2 + 1) // 2
        found_place = False
        if not self.width % 2:
            x -= 1
        if map[y][x] != " ":
            n = 2
            while y - n > 0:
                if map[y + n][x] == " ":
                    map[y + n][x] = self.pac_man
                    self.pac_man.spawn_position = (y + n, x)
                    self.pac_man.put_new_coordinates(y + n, x)
                    found_place = True
                    break

                if map[y - n][x] == " ":
                    map[y - n][x] = self.pac_man
                    self.pac_man.spawn_position = (y - n, x)
                    self.pac_man.put_new_coordinates(y - n, x)
                    found_place = True
                    break

                n += 2
                if not found_place:
                    raise ValueError("Problem on maze")
        else:
            self.pac_man.put_new_coordinates(y, x)
            self.pac_man.spawn_position = (y, x)
            map[y][x] = self.pac_man

    def ghosts_place(self, map):
        map[1][1] = self.pink_ghost
        self.pink_ghost.put_new_coordinates(1, 1)
        self.pink_ghost.respawn()

        map[1][self.width * 2 - 1] = self.red_ghost
        self.red_ghost.put_new_coordinates(1, self.width * 2 - 1)
        self.red_ghost.respawn()

        map[self.height * 2 - 1][1] = self.blue_ghost
        self.blue_ghost.put_new_coordinates(self.height * 2 - 1, 1)
        self.blue_ghost.respawn()

        map[self.height * 2 - 1][self.width * 2 - 1] = self.orange_ghost
        self.orange_ghost.put_new_coordinates(self.height * 2 - 1, self.width * 2 - 1)
        self.orange_ghost.respawn()
    
    def add_pac_man_and_ghosts(self, map):
        self.pac_man = Pac_Man()
        self.red_ghost = Ghost(color="Red")
        self.blue_ghost = Ghost(color="Blue")
        self.pink_ghost = Ghost(color="Pink")
        self.orange_ghost = Ghost(color="Orange")
        self.pac_man_place(map)
        self.ghosts_place(map)

    def generate_map(self) -> list[list[str]]:
        map = []
        tmp_list = ['#'] * (self.width * 2 + 1)

        for i in range(self.height * 2 + 1):
            map.append(tmp_list.copy())

        for i, y in enumerate(self.maze):
            for j, x in enumerate(y):
                map[i * 2 + 1][j * 2 + 1] = " "
                neighbors = self.get_neighbors(x)
                self.open_cells(map, neighbors, i, j)

        self.add_ft(map)
        self.add_pac_man_and_ghosts(map)
        return map

