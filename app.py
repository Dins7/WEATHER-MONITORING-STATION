from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
import urllib.request
import json
import time
import pandas as pd

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("weather_app.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    READ_API_KEY='3F8EF300XESNTPU6'
    CHANNEL_ID= '2510887'
    TS = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                         % (CHANNEL_ID,READ_API_KEY))
    
    file = r'/Users/dinesharavindh/Desktop/Med/seattle-weather.csv'
    data_1 = pd.read_csv(file)

    response = TS.read()
    data=json.loads(response)
    print(data)
    temp = data['field1']
    TS.close()

    random_index = np.random.randint(0, len(data_1))
    sample_data = data_1.iloc[random_index]
    int_features = sample_data[['precipitation', 'temp_min', 'wind']].values.reshape(1, -1)

    features = np.concatenate((int_features, np.array([[temp]])), axis=1)
    output = model.predict(features)[0]
    print("Value of output:",output)
    return render_template('weather_app.html', pred=f'Predicted weather: {output}')


if __name__ == '__main__':
    app.run(debug=True)