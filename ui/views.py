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

    def draw(self):
        for image in self.images + self.animations:
            image.draw(self.win_ptr)

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

        self.animations.extend(
            [
                AnimatedImage(
                    50,
                    20 + i * 20,
                    anim_dir / "pac-man_left",
                    frame_rate=1 / 15,
                )
                for i in range(10)
            ]
            + [
                AnimatedImage(
                    80,
                    20 + i * 20,
                    anim_dir / "pac-man_right",
                    frame_rate=1 / 2,
                )
                for i in range(10)
            ]
        )

    def update(self, dt: float) -> None:
        for image in self.animations:
            image.update(dt)

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
