from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from solver import solve_balas_hammer, solve_minico

app = FastAPI()

# Configuration CORS pour permettre au frontend HTML de communiquer avec l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransportData(BaseModel):
    costs: List[List[float]]
    supply: List[float]
    demand: List[float]

@app.post("/solve")
async def solve_transport(data: TransportData):
    # Résolution par les deux méthodes
    x_balas, z_balas, steps_balas = solve_balas_hammer(data.costs, data.supply, data.demand)
    x_minico, z_minico, steps_minico = solve_minico(data.costs, data.supply, data.demand)
    
    return {
        "balas": {"X": x_balas, "Z": z_balas, "steps": steps_balas},
        "minico": {"X": x_minico, "Z": z_minico, "steps": steps_minico}
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
