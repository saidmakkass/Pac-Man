from typing import Any

# from .mlx import mlx, mlx_ptr
# from .image import Image


class View:
    def __init__(self, win_ptr: Any, width: int, height: int):
        self.win_ptr = win_ptr
        self.width = width
        self.height = height

        self.frame_list = []

    def show(self):
        for image, x, y in self.frame_list:
            image.put_to_window(self.win_ptr, x, y)