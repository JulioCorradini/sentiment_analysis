import requests
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/analisis", methods=["POST"])
@cross_origin()
def reques_front_end(): 
  response = requests.get ("http://localhost:8080/respuesta")

  response_string = ""

  if response.status_code == 200:
    response_string = response.text
    print (response_string)
  else:
    print('La solicitud no se pudo realizar correctamente')

  sia = SentimentIntensityAnalyzer()

  sentimiento = sia.polarity_scores(response_string)['compound']

  def valoracion (sentimiento):
    valoracion = ""
      
    if (sentimiento > 0):
      valoracion = 'Valoracion Positiva'
    elif (sentimiento < 0):
      valoracion = 'Valoracion Negativa'
    else:
      valoracion = 'No se pudo determinar la intenicon del texto'
      
    data = {"txtoAnalisis": valoracion}
      
    valoration = requests.post ("http://localhost:8080/analisisPOST", json=data)
      
    if valoration.status_code == 200:
      print("POST exitoso")
    else:
      print("Error en el POST: ", valoration.status_code)

  valoracion(sentimiento)

if __name__ == '__main__':
    app.run()
