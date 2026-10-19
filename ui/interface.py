import time

from .globals import mlx, mlx_ptr
from .views.view import View
from .views.main_view import MainMenuView
from .views.game_view import GameView
from .views.pause_view import PauseView
from .views.over_view import GameOverView


class Interface:
    def __init__(self):
        self.width, self.height = 1280, 720
        self.win_ptr = mlx.mlx_new_window(
            mlx_ptr,
            self.width,
            self.height,
            "Pac-Man",
        )

        self.main_menu_view = MainMenuView(
            self.win_ptr,
            self.width,
            self.height,
            self,
        )
        self.game_view = GameView(
            self.win_ptr,
            self.width,
            self.height,
            self,
        )
        self.pause_menu_view = PauseView(
            self.win_ptr,
            self.width,
            self.height,
            self,
        )
        self.game_over_view = GameOverView(
            self.win_ptr,
            self.width,
            self.height,
            self,
        )
        self.views: list[View] = [
            self.main_menu_view,
            self.game_view,
            self.pause_menu_view,
            self.game_over_view,
        ]

        self.current_view = self.game_view

        self.last_time = time.perf_counter()

        self.setup_hooks()

    def setup_hooks(self):
        mlx.mlx_hook(self.win_ptr, 33, 0, self.exit, None)
        mlx.mlx_key_hook(self.win_ptr, self.key_hook, None)
        mlx.mlx_loop_hook(mlx_ptr, self.loop_hook, None)
        mlx.mlx_mouse_hook(self.win_ptr, self.mouse_hook, None)

    def loop_hook(self, _):
        now = time.perf_counter()
        dt = now - self.last_time
        self.last_time = now

        _, mx, my = mlx.mlx_mouse_get_pos(self.win_ptr)
        self.current_view.update(dt, mx, my)
        self.current_view.draw()

    def mouse_hook(self, button: int,  x: int, y: int, _) -> None:
        self.current_view.mouse_hook(button, x, y)

    def key_hook(self, keycode: int, _):
        self.current_view.key_hook(keycode)

    def run(self):
        self.current_view.draw()
        mlx.mlx_loop(mlx_ptr)

    def exit(self, _=None):
        for view in self.views:
            view.destroy()
        mlx.mlx_destroy_window(mlx_ptr, self.win_ptr)
        mlx.mlx_loop_exit(mlx_ptr)
