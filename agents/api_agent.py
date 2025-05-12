from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import yfinance as yf

app = FastAPI(title="Market Data API Agent")

class MarketDataRequest(BaseModel):
    tickers: List[str]
    period: str = "1d"
    interval: str = "1h"

@app.post("/get_market_data")
def get_market_data(request: MarketDataRequest):
    data = {}
    for ticker in request.tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=request.period, interval=request.interval)
        data[ticker] = hist.reset_index().to_dict(orient="records")
    return {
        "status": "success",
        "data": data
    }
