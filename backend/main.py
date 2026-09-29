from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mean import calculate_mean

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

class DataInput(BaseModel):
    numbers: list[float]

@app.post("/api/mean")
def calculate(data: DataInput):
    numbers = data.numbers

    result = calculate_mean(numbers)

    return {"mean": result}


@app.get("/")
def home():
    return {"message": "Statistics API is running"}