# EMA Strategy
## About
This app is developed by Immanuel Almosara (ialmosara) and Amitpal Gill (Amit97-ops). The idea behind this app is to utilize the 9, 21, and 55 EMA (Exponential Moving Average) to generate buying and selling signals.

## Technolgies used
The technologies used in this project include: 
* Python Flask
* Alpaca API (https://github.com/alpacahq/alpaca-trade-api-python/tree/9c78d4122c7d396f014435feed4058953f6612c0)
* PostgreSQL

## Signal Rules
If the 9 EMA crosses above the 21 and 55 EMA then it will trigger a buy signal.

If the price closes below the 9 EMA it triggers a sell signal.