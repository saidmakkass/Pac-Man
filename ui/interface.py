from .mlx import mlx, mlx_ptr
from .view import View
from .image import images


class Interface:
    def __init__(self):
        _, self.width, self.height = mlx.mlx_get_screen_size(mlx_ptr)
        self.win_ptr = mlx.mlx_new_window(
            mlx_ptr,
            self.width,
            self.height,
            "Pac-Man",
        )

        # views
        self.main_menu_view = View(self.win_ptr, self.width, self.height)
        self.game_view = View(self.win_ptr, self.width, self.height)
        self.pause_menu_view = View(self.win_ptr, self.width, self.height)
        self.game_over_view = View(self.win_ptr, self.width, self.height)

        self.current_view = self.main_menu_view

        self.__setup_hooks()

    def __setup_hooks(self):
        mlx.mlx_hook(self.win_ptr, 33, 0, self.exit, None)

    def run(self):
        self.current_view.show()
        mlx.mlx_loop(mlx_ptr)

    def exit(self, _):
        print(len(images), images)
        for image in images:
            mlx.mlx_destroy_image(mlx_ptr, image)
        mlx.mlx_destroy_window(mlx_ptr, self.win_ptr)
        mlx.mlx_loop_exit(mlx_ptr)
