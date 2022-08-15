from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('../ready_data.csv')

@app.route('/')
def index():

    bedroom = sorted(data['bedrooms'].unique())
    floor = sorted(data['floors'].unique())
    built = sorted(data['yr_built'].unique())
    yr_reno = sorted(data['yr_renovated'].unique())
    return render_template('index.html',bedroom=bedroom,floor_count=floor,built_yr=built,yr_reno=yr_reno)
    
    
@app.route('/predict', methods=['POST'])
def predict():
    return ""

if __name__ == '__main__':
    app.run(debug=True, port=5000)