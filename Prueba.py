import requests
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/analisis", methods=["POST"])
@cross_origin()
def reques_front_end():
    ##return("Solicitud recibida correctamente")
    print ("solicitud de Javascript correcta")


if __name__ == '__main__':
    app.run()