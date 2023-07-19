from flask import Flask, render_template,request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_crop():
    Nitrogen = float(request.form.get('Nitrogen'))
    Phosphorus = float(request.form.get('Phosphorus'))
    Potassium = float(request.form.get('Potassium'))
    Temperature = float(request.form.get('Temperature'))
    Humidity = float(request.form.get('Humidity'))
    pH = float(request.form.get('pH'))
    Rainfall = float(request.form.get('Rainfall'))

    #prediction
    result = model.predict(np.array([[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,pH,Rainfall]]))
    rs = ""    
    for i in result:
        rs+=i
    return render_template('index.html', result=rs)

if __name__ == '__main__':
    app.run(debug=True)