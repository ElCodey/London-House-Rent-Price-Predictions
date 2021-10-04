from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np

APP = Flask(__name__)
API = Api(APP)

RENT_MODEL = joblib.load('house_rent_price.sav')

class Predict(Resource):

    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('number_bedrooms')
       

        args = parser.parse_args()  # creates dict

        X_new = np.fromiter(args.values(), dtype=float)  # convert input to array

        out = {'Prediction': RENT_MODEL.predict([X_new])[0]}

        return out, 200


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')

import requests

url = 'http://127.0.0.1:1080/predict'  # localhost and the defined port + endpoint
body = {
    "number_bedrooms": 2
}
response = requests.post(url, data=body)
response.json()