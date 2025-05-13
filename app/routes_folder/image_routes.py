"""
Rotas para geração de imagens.
"""
from flask import Blueprint, jsonify, request
from app.services.image_generation.generator import ImageGenerator

image_bp = Blueprint('image', __name__)
image_generator = ImageGenerator()

@image_bp.route('/generate', methods=['POST'])
def generate_image():
    """
    Rota para gerar uma imagem com texto.
    Espera um JSON com o campo 'text'.
    """
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Texto não fornecido'}), 400
    
    try:
        image_base64 = image_generator.generate_image_base64(data['text'])
        return jsonify({
            'success': True,
            'image': image_base64
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500 