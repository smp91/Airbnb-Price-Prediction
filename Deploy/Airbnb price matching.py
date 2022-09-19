from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)


@app.route('/')
def temp():
    return render_template('template.html')

@app.route('/',methods=['POST','GET'])
def get_input():
    if request.method == 'POST':
        info = request.form['search']
        return redirect(url_for('run_pred',values=info))

@app.route('/run_pred/<values>')
def run_pred(values):
    import numpy as np 
    
    values = values.split(',')
    values = np.array(values)
    values = values.reshape(1,-1)
    
    with open('Airbnb_XGBoost_model', 'rb') as file:
        pickle_model = pickle.load(file)
        
    model = pickle_model
    pred = round(float(model.predict(np.float32(values))),2)
    
    return f'A good price for your listing could be ${pred}'
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)