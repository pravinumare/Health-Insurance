from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
from datetime import date, datetime
from utils import Age, Gender_encoding, BMI


app = Flask(__name__)


rf_model = pickle.load(open("rf_model.pkl", "rb"))
columns_list = pickle.load(open("columns_list.obj", "rb"))


@app.route('/premium')
def premium():

    data = request.get_json()

    birthday = data['Birthday']
    gender = data['Gender']
    height  = data['Height']
    weight = data['Weight']
    health_insurance_cover = data['Health_Insurance_Cover']

    age = Age(birthday)
    gender = Gender_encoding(gender)
    bmi = BMI(height, weight)


    test_df = pd.DataFrame({'Age(yrs)':[age],
                        'Gender':[gender],
                        'Health Insurance cover':[health_insurance_cover],
                        'BMI':[bmi]})
    
    prediction = rf_model.predict(test_df)
    print(type(prediction[0]))
    
    return jsonify({"Premium" : prediction[0]})


if __name__ == ("__main__"):
    app.run()

