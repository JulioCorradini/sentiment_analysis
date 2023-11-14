import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

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

  sia = SentimentIntensityAnalyzer()

  sentimiento = sia.polarity_scores(texto_recibido)['compound']

  def valoracion (sentimiento):
    valoracion = ""
      
    if (sentimiento > 0):
      valoracion = 1
    elif (sentimiento < 0):
      valoracion = -1
    else:
      valoracion = 0

    return {'valoracion': valoracion}
  
  result = valoracion (sentimiento)

  return jsonify(result)

if __name__ == '__main__':
    app.run()
