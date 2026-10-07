from .mlx import mlx, mlx_ptr
from .views import MainMenuView, GameView, PauseView, GameOverView, View


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
        )
        self.game_view = GameView(
            self.win_ptr,
            self.width,
            self.height,
        )
        self.pause_menu_view = PauseView(
            self.win_ptr,
            self.width,
            self.height,
        )
        self.game_over_view = GameOverView(
            self.win_ptr,
            self.width,
            self.height,
        )
        self.views: list[View] = [
            self.main_menu_view,
            self.game_view,
            self.pause_menu_view,
            self.game_over_view,
        ]

        self.current_view = self.main_menu_view

        self.setup_hooks()

    def setup_hooks(self):
        mlx.mlx_hook(self.win_ptr, 33, 0, self.exit, None)
        mlx.mlx_key_hook(self.win_ptr, self.key_hook, None)
        mlx.mlx_loop_hook(mlx_ptr, self.loop_hook, None)

    def loop_hook(self, _):
        mlx.mlx_clear_window(mlx_ptr, self.win_ptr)
        self.current_view.loop_hook()

    def key_hook(self, keycode: int, _):
        match self.current_view:
            case self.main_menu_view:
                self.main_menu_view.key_hook(keycode)

    def run(self):
        self.current_view.show()
        mlx.mlx_loop(mlx_ptr)

    def exit(self, _=None):
        for view in self.views:
            view.destroy()
        mlx.mlx_destroy_window(mlx_ptr, self.win_ptr)
        mlx.mlx_loop_exit(mlx_ptr)
