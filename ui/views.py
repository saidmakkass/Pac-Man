from typing import Any
from importlib.resources import files
from abc import ABC, abstractmethod

# from .mlx import mlx, mlx_ptr
from .image import Image, AnimatedImage

assets_dir = files(__package__) / "assets"
static_dir = assets_dir / "static"
anim_dir = assets_dir / "anim"


class View(ABC):
    def __init__(self, win_ptr: Any, width: int, height: int):
        self.win_ptr = win_ptr
        self.width = width
        self.height = height

        self.images: list[Image] = []
        self.animations: list[AnimatedImage] = []

    def show(self):
        for image in self.images + self.animations:
            image.draw(self.win_ptr)

    def loop_hook(self, dt: float):
        self.update(dt)
        self.show()

    def destroy(self):
        for image in self.images + self.animations:
            image.destroy()

    @abstractmethod
    def update(self, dt: float) -> None: ...

    @abstractmethod
    def key_hook(self, keycode: int): ...


class MainMenuView(View):
    def __init__(self, win_ptr, width, height):
        super().__init__(win_ptr, width, height)
        self.images.extend(
            [
                Image(0, 0, static_dir / "main_menu" / "background.png"),
                Image(369, 128, static_dir / "main_menu" / "title.png"),
                Image(462, 360, static_dir / "main_menu" / "start_button.png"),
                Image(462, 423, static_dir / "main_menu" / "score_button.png"),
                Image(462, 486, static_dir / "main_menu" / "info_button.png"),
                Image(462, 549, static_dir / "main_menu" / "exit_button.png"),
            ],
        )

    def update(self, dt: float) -> None:
        pass

    def key_hook(self, keycode: int) -> None:
        pass


class GameView(View):
    def update(self, dt: float) -> None:
        pass

    def key_hook(self, keycode: int) -> None:
        pass


class PauseView(View):
    def update(self, dt: float) -> None:
        pass

    def key_hook(self, keycode: int) -> None:
        pass


class GameOverView(View):
    def update(self, dt: float) -> None:
        pass

    def key_hook(self, keycode: int) -> None:
        pass
