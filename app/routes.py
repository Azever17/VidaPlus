from flask import render_template
from app.database import get_db
from app.models.hospital import Hospital
from app.models.medico import Medico
from app.models.paciente import Paciente
from app.models.leito import Leito
from app.models.consulta import Consulta
from app.models.internacao import Internacao
from app.routes_folder.image_routes import image_bp

def init_routes(app):
    # Registra o blueprint de imagens
    app.register_blueprint(image_bp, url_prefix='/api/images')
    
    @app.route('/')
    def index():
        db = next(get_db())
        try:
            hospitais = db.query(Hospital).all()
            medicos = db.query(Medico).all()
            pacientes = db.query(Paciente).all()
            leitos = db.query(Leito).all()
            consultas = db.query(Consulta).all()
            internacoes = db.query(Internacao).all()
            
            return render_template('index.html',
                                hospitais=hospitais,
                                medicos=medicos,
                                pacientes=pacientes,
                                leitos=leitos,
                                consultas=consultas,
                                internacoes=internacoes)
        finally:
            db.close()

    @app.route('/gerador-imagens')
    def image_generator_page():
        return render_template('image_generator.html') 