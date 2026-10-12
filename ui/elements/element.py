from abc import ABC, abstractmethod
from typing import Any


class Element(ABC):

    @abstractmethod
    def update(self, dt: float, mx: int, my: int) -> None: ...

    @abstractmethod
    def draw(self, win_ptr: Any) -> None: ...

    @abstractmethod
    def destroy(self) -> None: ...
