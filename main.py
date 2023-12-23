from datetime import datetime
from enum import Enum

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

import pandas as pd

app = FastAPI()


class EnergyMarket(str, Enum):
    caiso = "caiso"
    spp = "spp"
    ercot = "ercot"
    ieso = "ieso"
    aeso = "aeso"
    nyiso = "nyiso"
    pjm = "pjm"
    miso = "miso"
    isone = "isone"


class EnergyUsage(BaseModel):
    usage_kw: float
    market_name: EnergyMarket
    timestamp: datetime


@app.get("/")
def default_route():
    return {"slogan": "Better Energy, More Cash."}


@app.on_event("startup")
def on_startup():
    global market_map
    global usage
    market_map = (
        pd.read_csv("markets.csv").set_index("name").squeeze()
    )  # could also be: dict(pd.read_csv("markets.csv").set_index("name")["id"]) to store as a dict instead of series
    usage = pd.read_csv("usage.csv").sort_values(
        "usage_kw", ascending=False
    )  # while mantaining the index, sorts the dataframe by the values of usage_kw. Setting the kw ascending to 'false' returns it in descending order
    pass


@app.get("/peaks")
async def get_top5_peaks_for_market(market_name: str) -> List[EnergyUsage]:
    """Given a market name as a string, returns a list of EnergyUsage representing the 5 highest recorded kilowatt usages and the timestamp they were recorded at

    Args:
        market_name: a string corresponding to a single EnergyMarket

    Returns:
        A list of 5 (or less) EnergyUsage objects containing the market name, timestamp, and killowattage recorded in descending order (from highest to 5th highest)
    """
    # task:  complete this function and return correct, and correctly typed values.
    if usage is None or market_map is None:
        raise HTTPException(status_code=500, detail="market mapping and usage data not loaded")

    top_5_dataframe = usage[usage["market_id"] == market_map[market_name]].head(5)
    result = [
        EnergyUsage(
            usage_kw=row["usage_kw"],
            market_name=EnergyMarket(market_name),
            timestamp=row["timestamp"],
        )
        for index, row in top_5_dataframe.iterrows()
    ]
    # result: List[EnergyUsage] = []
    return result
