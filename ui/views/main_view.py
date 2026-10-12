from ui.elements.animation import Animation
from ui.elements.image import Image
from ui.elements.button import Button

from ui.globals import anim_dir, static_dir

from .view import View


class MainMenuView(View):

    def get_images(self) -> list[Image]:
        return [
            Image(0, 0, static_dir / "main_menu" / "background.png"),
            Image(369, 128, static_dir / "main_menu" / "title.png"),
        ]

    def get_animations(self):
        return [
            Animation(
                50,
                20 + i * 20,
                anim_dir / "pac-man_left",
                frame_rate=1 / (15 - i),
            )
            for i in range(10)
        ] + [
            Animation(
                80,
                20 + i * 20,
                anim_dir / "pac-man_right",
                frame_rate=1 / (2 + i),
            )
            for i in range(10)
        ]

    def get_buttons(self):
        return [
            Button(
                462,
                360,
                static_dir / "main_menu" / "start_button.png",
                static_dir / "main_menu" / "start_button_hover.png",
                self.start_click,
            ),
            Button(
                462,
                423,
                static_dir / "main_menu" / "score_button.png",
                static_dir / "main_menu" / "score_button_hover.png",
                self.score_click,
            ),
            Button(
                462,
                486,
                static_dir / "main_menu" / "info_button.png",
                static_dir / "main_menu" / "info_button_hover.png",
                self.info_click,
            ),
            Button(
                462,
                549,
                static_dir / "main_menu" / "exit_button.png",
                static_dir / "main_menu" / "exit_button_hover.png",
                self.exit_click,
            ),
        ]

    def key_hook(self, keycode: int) -> None:
        pass

    def mouse_hook(self, button: int, x: int, y: int):
        match button:
            case 1:
                for b in self.buttons:
                    b.check_click(x, y)

    def start_click(self):
        print("start")

    def score_click(self):
        print("score")

    def info_click(self):
        print("info")

    def exit_click(self):
        print("exit")
