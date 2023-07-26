import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('Aqi2.pkl','rb'))


@app.route('/')
def home():
  return render_template("index2.html")

@app.route('/predict',methods=['GET'])
def predict():


    '''
    For rendering results on HTML GUI
    '''
    city = float(request.args.get('city'))
    pm25 = float(request.args.get('pm25'))
    pm10 = float(request.args.get('pm10'))
    no = float(request.args.get('no'))
    no2 = float(request.args.get('no2'))
    nox = float(request.args.get('nox'))
    nh3 = float(request.args.get('nh3'))
    co = float(request.args.get('co'))
    so3 = float(request.args.get('so3'))
    o3 = float(request.args.get('o3'))
    benzene = float(request.args.get('benzene'))
    toluene = float(request.args.get('toluene'))
    xylene = float(request.args.get('xylene'))





    prediction = model.predict([[city, pm25, pm10, no, no2, nox, nh3, co, so3, o3, benzene, toluene, xylene]])


    return render_template('index2.html', prediction_text='Predicted Air Quality Index : {}'.format(prediction))

if __name__ == "__main__":
    socketio.run(app)
