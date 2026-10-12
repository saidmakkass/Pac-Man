from .view import View


class GameOverView(View):

    def get_images(self):
        return []

    def get_animations(self):
        return []

    def get_buttons(self):
        return []

    def key_hook(self, keycode):
        pass

    def mouse_hook(self, button: int, x: int, y: int): ...