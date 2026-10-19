from datetime import datetime, timedelta
from typing import Any

from ui.elements.image import Image
from ui.elements.animation import Animation
from ui.elements.button import Button
from ui.elements.map import Map
from engine.mapgenerator import MapGenerator

from ui.globals import static_dir

from .view import View


class GameView(View):
    def __init__(self, win_ptr: Any, width: int, height: int, interface):
        self.start_time = None
        self.timer = 0
        self.score = 0
        self.level = 0
        self.lives = 0

        super().__init__(win_ptr, width, height, interface)
        self.map = Map(
            340,
            60,
            25,
            25,
            static_dir / "game_view" / "map_background.png",
        )
        self.elements.append(self.map)

    def get_images(self):
        return [
            Image(0, 0, static_dir / "game_view" / "background.png"),
            Image(28, 60, static_dir / "game_view" / "left_panel.png"),
            Image(1002, 60, static_dir / "game_view" / "right_panel.png"),
            # Image(58, 222, static_dir / "game_view" / "level_background.png"),
            # Image(
            #     1032, 222, static_dir / "game_view" / "lives_background.png"
            # ),
        ]

    def get_animations(self):
        return []

    def get_buttons(self):
        return []

    # def get_texts(self):
    #     self.timer_text = Text(
    #         58,
    #         222,
    #         "placeholder",
    #         0xFF00FFFF,
    #         32,
    #         static_dir / "game_view" / "timer_background.png",
    #         margin=5,
    #     )
    #     self.score_text = Text(
    #         1032,
    #         119,
    #         "Placeholder",
    #         0xFF00FFFF,
    #         32,
    #         static_dir / "game_view" / "score_background.png",
    #         margin=5,
    #     )
    #     return [
    #         self.timer_text,
    #         self.score_text,
    #     ]

    def update(self, dt: float, mx: int, my: int) -> None:
        self.timer += dt
        frame_time = 1 / 60
        if self.timer < frame_time:
            return
        self.timer -= frame_time

        for element in self.elements:
            element.update(dt, mx, my)
        # self.map = self.engine.generate_map()
        # for i in self.map:
        # print(i)
        # print("\n-------------------------\n")

        # if self.start_time is None:
        #     self.start_time = datetime.now()

        # self.timer_text.update(
        #     dt,
        #     mx,
        #     my,
        #     f"{int(self.timer) // 60}:{int(self.timer) % 60:02d}",
        # )

    def key_hook(self, keycode):
        pass

    def draw(self):
        # print(self.timer)

        return super().draw()

    def mouse_hook(self, button: int, x: int, y: int): ...
