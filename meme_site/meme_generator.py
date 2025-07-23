from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_meme(image_path, top_text, bottom_text, output_path):
    # Загружаем изображение
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size

    # Загрузка шрифта
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Подстрой под свой путь
    max_font_size = int(image_height * 0.08)

    def draw_text(text, y_pos, max_width=40):
        font_size = max_font_size
        while font_size > 10:
            font = ImageFont.truetype(font_path, font_size)
            wrapped_text = textwrap.fill(text, width=max_width)
            text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            if text_width <= image_width - 40:
                break
            font_size -= 2

        # Центрирование текста
        text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        x = (image_width - text_width) // 2
        draw.text((x, y_pos), wrapped_text, font=font, fill="white", stroke_width=2, stroke_fill="black")

    # Верхний и нижний текст
    if top_text:
        draw_text(top_text.upper(), 10)
    if bottom_text:
        draw_text(bottom_text.upper(), image_height - max_font_size * 2)

    img.save(output_path)
