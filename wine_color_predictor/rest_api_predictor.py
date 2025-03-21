from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import pandas
from wine_color_predictor import train

_data = train.load_winequality_data()
_model = train.train_model(_data)

app = FastAPI()

class WineQualityInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality: float

@app.post("/predict")
def predict(input: WineQualityInput):
    input_data = pandas.DataFrame([input.model_dump()])
    predictions = _model.predict(input_data)
    if predictions[0] == 1:
        return {"color": "red"}
    else:
        return {"color": "white"}
