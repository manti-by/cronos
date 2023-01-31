from datetime import datetime

from PIL import Image, ImageFont, ImageDraw


class Imager:

    bg_color = (30, 30, 30)

    info_color = (255, 255, 255)
    warning_color = (255, 255, 0)
    critical_color = (255, 0, 0)

    primary_font = ImageFont.truetype("resources/roboto.ttf", 54)
    secondary_font = ImageFont.truetype("resources/roboto.ttf", 24)

    def __init__(self, data: dict):
        self.data = data

    def get_color(self, data: dict) -> tuple:
        if data["value"] > data["critical"]:
            return self.critical_color
        if data["value"] > data["warning"]:
            return self.warning_color
        return self.info_color

    def generate(self) -> Image:
        image = Image.new(mode="RGB", size=(320, 240), color=self.bg_color)
        draw = ImageDraw.Draw(image)
        draw.text(
            (10, 10),
            f"T1: {self.data['T1']['value']}",
            self.get_color(self.data["T1"]),
            font=self.primary_font,
        )
        draw.text(
            (10, 100),
            f"T2: {self.data['T2']['value']}",
            self.get_color(self.data["T2"]),
            font=self.primary_font,
        )

        draw.text(
            (220, 10),
            f"T3: {self.data['T3']['value']}",
            self.get_color(self.data["T3"]),
            font=self.secondary_font,
        )
        draw.text(
            (220, 70),
            f"T4: {self.data['T4']['value']}",
            self.get_color(self.data["T4"]),
            font=self.secondary_font,
        )
        draw.text(
            (220, 130),
            f"T5: {self.data['T5']['value']}",
            self.get_color(self.data["T5"]),
            font=self.secondary_font,
        )
        draw.text(
            (10, 190),
            f"{datetime.now().strftime('%H:%M / %d %b %Y')}",
            self.info_color,
            font=self.secondary_font,
        )
        return image
