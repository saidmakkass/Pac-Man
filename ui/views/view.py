from abc import ABC, abstractmethod
from typing import Any

from ui.elements.element import Element
from ui.elements.image import Image
from ui.elements.animation import Animation
from ui.elements.button import Button


class View(ABC):
    def __init__(self, win_ptr: Any, width: int, height: int):
        self.win_ptr = win_ptr
        self.width = width
        self.height = height

        self.images = self.get_images()
        self.animations = self.get_animations()
        self.buttons = self.get_buttons()
        self.elements = self.images + self.animations + self.buttons

    @abstractmethod
    def get_images(self) -> list[Image]: ...

    @abstractmethod
    def get_animations(self) -> list[Animation]: ...

    @abstractmethod
    def get_buttons(self) -> list[Button]: ...

    @abstractmethod
    def key_hook(self, keycode: int): ...

    @abstractmethod
    def mouse_hook(self, button: int, x: int, y: int): ...

    def update(self, dt: float, mx: int, my: int) -> None:
        for element in self.elements:
            element.update(dt, mx, my)

    def draw(self):
        for element in self.elements:
            element.draw(self.win_ptr)

    def destroy(self):
        for element in self.elements:
            element.destroy()
