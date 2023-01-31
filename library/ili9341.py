from PIL.Image import Image


class ILI9341:
    def __init__(self, image: Image):
        self.image = image

    def update(self):
        self.image.show()
