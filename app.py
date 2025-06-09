from flask import Flask
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials,firestore
import os
import json


load_dotenv() # Cargar las variables

app = Flask(__name__)
port = int(os.environ.get('PORT',5000))
key = os.getenv("FIREBASE_KEY", 'No se encontro clave')

key_dict = json.loads(key)

cred = credentials.Certificate(key_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/')
def home():
    mensaje = os.getenv("MI_MENSAJE", 'No se obtuvo la variable')
    return f'Pagina de inicio, {mensaje}'

@app.route('/submit', methods=['POST'])
def recive():
    doc_ref = db.collection('usuarios').document('usuario_1')
    doc_ref.set({
        'nombre': 'Daniel',
        'contraseña': 'Brayner17.'
    })
    return 'Datos guardados correctamente'
