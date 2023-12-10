from flask import Flask
from flask_cors import CORS

from config import config
from modelo.EstudianteModel import EstudianteModel

app = Flask(__name__)

# HABILITAR EL INTERCAMBIO DE RECUROS  DE ORIGEN CRUZADOS para las peticiones
# GET, POST, DELETE, PUT en especial
#CORS(app, resources={r"/estudiante/*": {"origins": "http://http://localhost"}})
CORS(app, resources={r"/estudiante/*": {"origins": "https://proyecto-modulo3.onrender.com"}})


@app.route('/estudiante', methods=['GET'])
def listar_estudiante():
    x= EstudianteModel.listar_estudiante()
    return x


@app.route('/estudiante/:<codigo>', methods=['GET'])
def lista_estudiante(codigo):
    x= EstudianteModel.lista_estudiante(codigo)
    return x


@app.route('/estudiante', methods=['POST'])
def registrar_estudiante():
    x= EstudianteModel.registrar_estudiante()
    return x


@app.route('/estudiante/:<codigo>', methods=['DELETE'])
def eliminar_curso(codigo):
    x= EstudianteModel.eliminar_estudiante(codigo)
    return x


@app.route('/estudiante/:<codigo>', methods=['PUT'])
def actulalizar_estudiante(codigo):
    x= EstudianteModel.actualizar_estudiante(codigo)
    return x



@app.route('/estudiante/promedio-edad', methods=['GET'])
def promedio_edad():
    x= EstudianteModel.promedio_edad()
    return x


@app.route('/estado', methods=['GET'])
def estado():
    x= EstudianteModel.estado()
    return x



def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='0.0.0.0')