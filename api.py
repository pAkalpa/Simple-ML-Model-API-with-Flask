'''
/*
 * @Author: Pasindu Akalpa 
 * @Date: 2021-01-24 19:37:38 
 * @Last Modified by: Pasindu Akalpa
 * @Last Modified time: 2021-01-24 20:06:14
 */
'''
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import joblib
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def feedModel():
    data = request.get_json()
    prediction = np.array2string(model.predict(data)[0])

    return jsonify(prediction)

if __name__ == '__main__':
    model = joblib.load(r'D:\My Python NoteBooks\Simple ML Model API\IRIS_KNN.sav')
    app.run(debug=True, host='0.0.0.0')#change to '0.0.0.0' your IPv4 address