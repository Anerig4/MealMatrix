from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class UserInput(BaseModel):
    mood: str

food_db = {
    "happy": ["Pizza", "Pasta", "Ice Cream"],
    "sad": ["Soup", "Khichdi", "Tea"],
    "tired": ["Sandwich", "Coffee", "Maggi"]
}

@app.post("/recommend")
def recommend(data: UserInput):
    mood = data.mood.lower()
    return {"recommendations": food_db.get(mood, ["Rice", "Dal"])}
