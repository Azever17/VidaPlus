"""
Módulo para geração de imagens.
"""
from PIL import Image, ImageDraw, ImageFont
import io
import base64
from typing import Optional, Tuple

class ImageGenerator:
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.background_color = (255, 255, 255)  # Branco
        self.text_color = (0, 0, 0)  # Preto

    def create_blank_image(self) -> Image.Image:
        """Cria uma imagem em branco com as dimensões especificadas."""
        return Image.new('RGB', (self.width, self.height), self.background_color)

    def add_text(self, image: Image.Image, text: str, position: Tuple[int, int], 
                font_size: int = 32) -> Image.Image:
        """Adiciona texto à imagem."""
        draw = ImageDraw.Draw(image)
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()
        
        draw.text(position, text, font=font, fill=self.text_color)
        return image

    def generate_image(self, text: str, output_format: str = 'PNG') -> bytes:
        """Gera uma imagem com o texto especificado."""
        image = self.create_blank_image()
        # Centraliza o texto
        text_position = (self.width // 4, self.height // 2)
        image = self.add_text(image, text, text_position)
        
        # Converte para bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=output_format)
        return img_byte_arr.getvalue()

    def image_to_base64(self, image_bytes: bytes) -> str:
        """Converte bytes da imagem para string base64."""
        return base64.b64encode(image_bytes).decode('utf-8')

    def generate_image_base64(self, text: str) -> str:
        """Gera uma imagem e retorna em formato base64."""
        image_bytes = self.generate_image(text)
        return self.image_to_base64(image_bytes) 