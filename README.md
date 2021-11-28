# Btcie
Process to monitor Bitcoin and altcoin prices and notify of buy/sell signals from desired indicators, such as bollinger bands and price momentum.  Why not automate trading fully? This tool is intended to asist a human with infrequent long plays, not replace them entirely for higher frequency trading.

Also it is generally confusing to track altcoin prices in both USD$ and Bitcoin, and decide whether a given trade might yield more $$ but lose value in bitcoin. Which trade would be more advantageous when it is time to take profits?

# Quick setup
1. Clone repo
2. Create virtual environment and install dependencies
    * python3 -m venv env
    * source env/bin/activate     (for mac/linux)
    * pip install --upgrade pip
    * pip install -r requirements.txt
3. Run
    * python src/main.py

## Pain points to target:
* Actively monitoring prices and trends is time-consuming, and can let emotions creep into decision making
* Determining cost basis of current positions is hard, both for tax purposes and to track how well portfolio is doing

## What it is not:
* Not an active trading bot
* Not something that needs to know any user account info
* Not financial or tax advice

## Features:
See doc / Use Cases

## Data:
Downloaded historical bitcoin price data from https://finance.yahoo.com/quote/BTC-USD/history and stored as CSV file in lib folder.
