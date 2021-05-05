import alpaca_trade_api as tradeapi
import talib
import numpy
from decouple import config
from flask import Flask, request

app = Flask(__name__)

@app.run('/run=<symbol>')
def run(self):
    pass
    
if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port='90')