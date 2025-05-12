from fastapi import FastAPI, Request
import requests

app = FastAPI(title="Orchestrator Agent")

@app.post("/morning_brief")
async def morning_brief(request: Request):
    data = await request.json()
    user_question = data.get("question", "").lower()

    if "asia tech" in user_question:
        analysis_res = requests.post("http://localhost:8001/calculate_exposure", json={
            "region": "Asia",
            "sector": "Technology"
        }).json()

        exposure = analysis_res.get("exposure_percentage", 0)
        previous_exposure = 18.0
        delta = float(exposure) - previous_exposure

        earnings_res = requests.post("http://localhost:8004/scrape_earnings", json={
            "tickers": ["TSM", "SSNLF"]
        }).json()

        earnings_summary = "TSMC beat estimates by 4 %, Samsung missed by 2 %."
        narrative = f"Today, your Asia tech allocation is {exposure:.1f} % of AUM, "
        narrative += f"{'up' if delta > 0 else 'down'} from {previous_exposure} % yesterday. "
        narrative += earnings_summary
        narrative += " Regional sentiment is neutral with a cautionary tilt due to rising yields."

        requests.post("http://localhost:8005/speak", json={"text": narrative})
        return {"brief": narrative}

    return {"brief": "Sorry, I could not understand the question."}
