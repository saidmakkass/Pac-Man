from typing import Any, Optional, Protocol
from pathlib import Path

from ui.globals import mlx, mlx_ptr

from .element import Element


class Image(Element):
    def __init__(
        self,
        x: int,
        y: int,
        path: Optional[Path] = None,
        *,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ):
        self.x, self.y = x, y

        if path is not None:
            self.img_ptr, self.width, self.height = mlx.mlx_png_file_to_image(
                mlx_ptr, str(path)
            )
        else:
            assert width is not None, "missing width"
            assert height is not None, "missing height"
            self.width, self.height = width, height
            self.img_ptr = mlx.mlx_new_image(mlx_ptr, self.width, self.height)

        img_buf, _, _, _ = mlx.mlx_get_data_addr(self.img_ptr)

        self.img_buf = img_buf.cast("I", shape=[self.height, self.width])
        self.path = path  # for debugging

    def put_pixel(self, x: int, y: int, color: int) -> None:
        self.img_buf[y, x] = color

    def update(self, dt: float, mx: int, my: int) -> None:
        pass

    def draw(self, win_ptr: Any) -> None:
        mlx.mlx_put_image_to_window(
            mlx_ptr,
            win_ptr,
            self.img_ptr,
            self.x,
            self.y,
        )

    def destroy(self):
        mlx.mlx_destroy_image(mlx_ptr, self.img_ptr)

    def clear(self, color: int):
        print(self.width, self.height, self.path, len(self.img_buf))  # debug
        for x in range(self.width):
            for y in range(self.height):
                self.put_pixel(x, y, color)
