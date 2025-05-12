from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
import pandas as pd
import numpy as np

app = FastAPI(title="Analysis Agent")

# Example Portfolio Data (you can replace this with actual data)
portfolio_data = [
    {"ticker": "AAPL", "sector": "Technology", "region": "North America", "weight": 0.15},
    {"ticker": "TSM", "sector": "Technology", "region": "Asia", "weight": 0.10},
    {"ticker": "GOOGL", "sector": "Technology", "region": "North America", "weight": 0.20},
    {"ticker": "BABA", "sector": "Technology", "region": "Asia", "weight": 0.05},
    {"ticker": "AMZN", "sector": "Consumer Discretionary", "region": "North America", "weight": 0.10},
    {"ticker": "SNE", "sector": "Technology", "region": "Asia", "weight": 0.05},
    {"ticker": "MSFT", "sector": "Technology", "region": "North America", "weight": 0.15},
    {"ticker": "HYD", "sector": "Healthcare", "region": "Asia", "weight": 0.05},
    {"ticker": "NTES", "sector": "Technology", "region": "Asia", "weight": 0.05},
]

# Convert to DataFrame for easier analysis
df = pd.DataFrame(portfolio_data)

class AnalysisRequest(BaseModel):
    region: str
    sector: str

@app.post("/calculate_exposure")
def calculate_exposure(request: AnalysisRequest):
    # Filter portfolio by region and sector
    filtered_data = df[(df["region"] == request.region) & (df["sector"] == request.sector)]
    
    if filtered_data.empty:
        return {"error": "No data found for this region and sector combination."}
    
    # Calculate the total weight of the filtered data (tech exposure in Asia, for example)
    total_exposure = filtered_data["weight"].sum()
    
    return {"region": request.region, "sector": request.sector, "exposure_percentage": total_exposure * 100}

