from typing import Any, Optional, Protocol
from pathlib import Path


from .mlx import mlx, mlx_ptr


class Image:
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

    def draw(self, win_ptr: Any) -> None:
        mlx.mlx_put_image_to_window(
            mlx_ptr,
            win_ptr,
            self.img_ptr,
            self.x,
            self.y,
        )

    def clear(self, color: int):
        print(self.width, self.height, self.path, len(self.img_buf))  # debug
        for x in range(self.width):
            for y in range(self.height):
                self.put_pixel(x, y, color)

    def destroy(self):
        mlx.mlx_destroy_image(mlx_ptr, self.img_ptr)


class AnimatedImage:
    def __init__(self, x: int, y: int, dir_path: str):
        self.x, self.y = x, y

        image_paths = sorted(list(Path(dir_path).glob("*.png")))
        self.frames: list[Image] = []
        self.current_frame = 0
        for path in image_paths:
            self.frames.append(Image(self.x, self.y, path))
        self.n_frames = len(self.frames)

    def draw(self, win_ptr: Any) -> None:
        self.frames[self.current_frame].draw(win_ptr)
        self.current_frame += 1
        self.current_frame %= self.n_frames

    def destroy(self) -> None:
        for image in self.frames:
            image.destroy()
