import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__,template_folder='templates')
f = open('model2.pkl', 'rb')
model2=pickle.load(f)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model2.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index2.html', prediction_text='Chances of covid is {}'.format(output))

if __name__ == '__main__':
    app.run()


