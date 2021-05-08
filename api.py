import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
from decouple import config
from datetime import datetime, timezone, timedelta
from flask import Flask, request
import psycopg2

app = Flask(__name__)

ENDPOINT = config('ENDPOINT')
PAPER_ENDPOINT = config('PAPER_ENDPOINT')
SECRET_KEY = config('SECRET_KEY')
API_KEY = config('API_KEY_ID')
PAPER_STREAM_ENDPOINT = config('PAPER_STREAM_ENDPOINT')

alpaca = tradeapi.REST(API_KEY, SECRET_KEY, PAPER_ENDPOINT, 'v2')
stream = tradeapi.stream.TradingStream(API_KEY, SECRET_KEY, PAPER_STREAM_ENDPOINT)

conn = psycopg2.connect(host='localhost',
                        database='emastrategy',
                        user='manny',
                        password='emastrategy')

@app.route('/subscribe')
def subscribe():
    # Used for subscribing to data
    return

@app.route('/get_data')
def get_data():
    # Fetching historical data
    j = request.get_json()
    local_time = datetime.now()
    # Parse timestamps (Last 3 months to compensate for 55 EMA)
    end_time, start_time = local_time.isoformat('T')+"Z", (local_time-timedelta(days=90)).isoformat('T') + "Z"
    bars = alpaca.get_bars(symbol=j['symbol'], timeframe=TimeFrame.Day, start=start_time, end=end_time)
    for bar in bars:
        print(bar)
    return ''

@app.route('/run')
def run():
    r = request.json()
    alpaca.cancel_all_orders()
    alpaca.submit_order(symbol=r['symbol'], qty=r['qty'], side=r['side'], type=r['type'], time_in_force=r['time_in_force'])
    
if __name__ == '__main__':
    app.run(port=90)