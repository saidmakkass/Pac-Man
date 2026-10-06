from typing import Any, Optional

from .mlx import mlx, mlx_ptr

images = []

class Image:
    def __init__(
        self,
        path: Optional[str] = None,
        *,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ):
        if path is not None:
            self.img_ptr, self.width, self.height = mlx.mlx_png_file_to_image(
                mlx_ptr, path
            )
        else:
            assert width is not None, "missing width"
            assert height is not None, "missing height"
            self.width, self.height = width, height
            self.img_ptr = mlx.mlx_new_image(mlx_ptr, self.width, self.height)

        images.append(self.img_ptr)

        img_buf, _, _, _ = mlx.mlx_get_data_addr(self.img_ptr)

        self.img_buf = img_buf.cast("I", shape=[self.width, self.height])

    def put_pixel(self, x: int, y: int, color: int) -> None:
        self.img_buf[y, x] = color

    def put_to_window(self, win_ptr: Any, x: int, y: int) -> None:
        mlx.mlx_put_image_to_window(mlx_ptr, win_ptr, self.img_ptr, x, y)

    def clear(self, color: int):
        for x in range(self.width):
            for y in range(self.height):
                self.put_pixel(x, y, color)
