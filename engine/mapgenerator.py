from mazegenerator import MazeGenerator

class MapGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = MazeGenerator(size=(width, height)).maze
        self.map = self.generate_map()

    @staticmethod
    def open_cells(maze, neighbors, y, x):
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
    def convert_base(number):
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
    def get_neighbors(number):
        binary_n = MapGenerator.convert_base(number)
        directions = ["W", "S", "E", "N"]
        neighbors = []
        for i, c in enumerate(binary_n):
            if c == "0":
                neighbors.append(directions[i])

        return neighbors

    def generate_map(self):
        map = []
        tmp_list = ['#'] * (self.width * 2 + 1)

        for i in range(self.height * 2 + 1):
            map.append(tmp_list.copy())

        for i, y in enumerate(self.maze):
            for j, x in enumerate(y):
                map[i * 2 + 1][j * 2 + 1] = " "
                neighbors = self.get_neighbors(x)
                self.open_cells(map, neighbors, i, j)

        return map