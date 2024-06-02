from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('stock_data.csv', index_col=0, parse_dates=True)
    return render_template('index.html', data=df.to_html())

if __name__ == '__main__':
    app.run(debug=True)
