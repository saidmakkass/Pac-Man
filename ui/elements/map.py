from pathlib import Path
from typing import Any

from engine import MapGenerator
from ui.globals import static_dir

from .element import Element
from .image import Image


class Map(Element):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        background_path: Path,
    ):
        self.background = Image(
            x,
            y,
            background_path,
        )
        self.map = MapGenerator(
            width,
            height,
        )
        self.image = Image(
            x,
            y,
            width=self.background.width,
            height=self.background.height,
        )

    def render_wall(self, x, y):
        wall_size = 10
        cell_size = 10
        for w in range(wall_size):
            for h in range(wall_size):
                self.image.put_pixel(
                    x * wall_size + w + cell_size,
                    y * wall_size + h + cell_size,
                    0xFF0000FF,
                )

    def render_ft(self, x, y):
        wall_size = 10
        cell_size = 10
        for w in range(wall_size):
            for h in range(wall_size):
                self.image.put_pixel(
                    x * wall_size + w + cell_size,
                    y * wall_size + h + cell_size,
                    0xFFFF00FF,
                )

    def render_cell(self, x, y):
        pass

    def render_map(self):
        self.image.clear(0)
        for y, row in enumerate(self.map.map):
            for x, cell in enumerate(row):
                match cell:
                    case "#":
                        self.render_wall(x, y)
                    case "@":
                        self.render_ft(x, y)
                    case " ":
                        self.render_cell(x, y)

    def update(self, dt: float, mx: int, my: int) -> None:
        self.render_map()

    def draw(self, win_ptr: Any) -> None:
        self.background.draw(win_ptr)
        self.image.draw(win_ptr)

    def destroy(self) -> None:
        self.background.destroy()
        self.image.destroy()
