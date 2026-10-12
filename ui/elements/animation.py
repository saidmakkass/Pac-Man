from typing import Any
from pathlib import Path

from .element import Element
from .image import Image


class Animation(Element):
    def __init__(self, x: int, y: int, dir_path: str, *, frame_rate: float):
        self.x, self.y = x, y

        image_paths = sorted(list(Path(dir_path).glob("*.png")))

        self.frames: list[Image] = []
        for path in image_paths:
            self.frames.append(Image(self.x, self.y, path))
        self.n_frames = len(self.frames)
        self.frame_interval = frame_rate
        self.current_frame = 0
        self.frame_timer = 0

    def update(self, dt: float, mx: int, my: int) -> None:
        self.frame_timer += dt

        if self.frame_timer >= self.frame_interval:
            self.frame_timer -= self.frame_interval
            self.current_frame = (self.current_frame + 1) % self.n_frames

    def draw(self, win_ptr: Any) -> None:
        self.frames[self.current_frame].draw(win_ptr)

    def destroy(self) -> None:
        for image in self.frames:
            image.destroy()
