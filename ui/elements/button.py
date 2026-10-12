from typing import Optional, Callable
from pathlib import Path

from .element import Element
from .image import Image


class Button(Element):
    def __init__(
        self,
        x,
        y,
        path,
        hover_path: Optional[Path] = None,
        on_click: Optional[Callable[[None], None]] = None,
    ):
        self.x, self.y = x, y
        self.idl_image = Image(x, y, path)
        self.hover_image = Image(x, y, hover_path if hover_path else path)
        self.image = self.idl_image
        self.on_click = on_click if on_click else lambda: None

    def update(self, dt: float, mx: int, my: int):
        if (
            self.x < mx < self.x + self.image.width
            and self.y < my < self.y + self.image.height
        ):
            self.image = self.hover_image
        else:
            self.image = self.idl_image

    def draw(self, win_ptr):
        self.image.draw(win_ptr)

    def destroy(self):
        pass

    def check_click(self, x: int, y: int):
        if (
            self.x < x < self.x + self.image.width
            and self.y < y < self.y + self.image.height
        ):
            self.on_click()
