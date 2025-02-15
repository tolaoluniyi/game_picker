from flask import Flask, render_template
from database.db_handler import get_historical_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    historical_data = get_historical_data()
    return render_template('results.html', data=historical_data)

def run_ui():
    app.run(debug=True)
