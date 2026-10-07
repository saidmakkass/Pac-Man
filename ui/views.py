from typing import Any
from importlib.resources import files

# from .mlx import mlx, mlx_ptr
from .image import Image, AnimatedImage

assets_dir = files(__package__) / "assets"
static_dir = assets_dir / "static"
anim_dir = assets_dir / "anim"


class View:
    def __init__(self, win_ptr: Any, width: int, height: int):
        self.win_ptr = win_ptr
        self.width = width
        self.height = height

        self.images: list[Image | AnimatedImage] = []

    def show(self):
        for image in self.images:
            image.put_to_window(self.win_ptr)

    def loop_hook(self):
        for image in self.images:
            image.put_to_window(self.win_ptr)

    def key_hook(self, keycode: int):
        match keycode:
            case 65307:  # escape key
                self.exit()
            case _:
                print(keycode)

    def destroy(self):
        for image in self.images:
            image.destroy()


class MainMenuView(View):
    def __init__(self, win_ptr, width, height):
        super().__init__(win_ptr, width, height)
        self.images.extend(
            [
                Image(0, 0, static_dir / "main_menu" / "background.png"),
                Image(369, 128, static_dir / "main_menu" / "title.png"),
                Image(462, 360, static_dir / "main_menu" / "start_button.png"),
                Image(462, 423, static_dir / "main_menu" / "score_button.png"),
                Image(462, 486, static_dir / "main_menu" / "instructions_button.png"),
                Image(462, 549, static_dir / "main_menu" / "exit_button.png"),
            ],
        )



class GameView(View):
    pass


class PauseView(View):
    pass


class GameOverView(View):
    pass
