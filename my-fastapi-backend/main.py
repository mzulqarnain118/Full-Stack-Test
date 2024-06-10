from fastapi import FastAPI, HTTPException, Query
import requests

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/cryptos")
def get_cryptos(page: int = Query(1, ge=1), per_page: int = Query(10, ge=1)):
    try:
        response = requests.get(
            'https://api.coingecko.com/api/v3/coins/markets',
            params={
                'vs_currency': 'usd',
                'order': 'market_cap_desc',
                'per_page': per_page,
                'page': page
            }
        )
        response.raise_for_status()
        data = response.json()

        # Ensure data is not empty and contains necessary keys
        if not data or not all('name' in item and 'current_price' in item for item in data):
            raise ValueError("Corrupted or incomplete data received")

        return data

    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail="External API request failed") from e
    except ValueError as e:
        raise HTTPException(status_code=500, detail=str(e))
