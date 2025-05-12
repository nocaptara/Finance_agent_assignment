from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import requests
from bs4 import BeautifulSoup

app = FastAPI(title="Earnings Scraping Agent")

class TickerRequest(BaseModel):
    tickers: List[str]

def get_yahoo_earnings(ticker: str):
    url = f"https://finance.yahoo.com/quote/{ticker}/analysis"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code != 200:
        return {"error": f"Failed to fetch data for {ticker}"}

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Attempt to find earnings data
    earnings_section = soup.find("section", string=lambda s: s and "Earnings Estimate" in s)
    
    # Simple fallback: return a mock or note
    return {"ticker": ticker, "note": "Parsing logic can be improved based on actual structure."}

@app.post("/scrape_earnings")
def scrape_earnings(request: TickerRequest):
    results = {}
    for ticker in request.tickers:
        results[ticker] = get_yahoo_earnings(ticker)
    return {"status": "success", "data": results}
