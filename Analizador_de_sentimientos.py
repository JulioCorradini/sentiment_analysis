import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Preprocezado_de_texto import preprocess_text
from Frecuencia_de_palabras import extract_features
from Entrenar_el_modelo import classifier

# Descargar el recurso vader_lexicon
nltk.download('vader_lexicon')

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/analisis", methods=["POST"])
@cross_origin()
def reques_front_end(): 

  data = request.get_json()
  
  texto_recibido = data['texto']

  # Preprocesamiento del texto ingresado
  preprocessed_text = preprocess_text(texto_recibido)

  # Extracción de características del texto ingresado
  features = extract_features(preprocessed_text)

  # Clasificación del nuevo texto
  sentiment = classifier.classify(features)

  def valoracion (sentiment):
    valoracion = ""
    if(sentiment == 'positive'):
      valoracion = 1
    elif (sentiment == 'negative'):
       valoracion = -1
    else:
       valoracion = 0
    return {'valoracion': valoracion}
  
  result = valoracion (sentiment)

  return jsonify(result)

if __name__ == '__main__':
    app.run()
