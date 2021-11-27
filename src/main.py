from typing import Optional

from fastapi import FastAPI

app = FastAPI()

db = { 
    "Countries": {
        "pt": { "Duelos de Honra", "Gargula", "Versus" },
        "es": { "lgs1", "lgs2", "lgs3" },
        "uk": { "Bootleg Duelos", "lgs2", "lgs3" }
    }
}

# - Root -
@app.get("/")
def read_root():
    return {"Hello": "World"}

# - Get all LGSs in DB -
@app.get("/lgs")
def read_root():

    response = db

    return response

# - Get LGS by country -
@app.get("/lgs/country/{country}")
def read_root(country: str):
    
    response = db["Countries"][country]

    return response

# - Get all LGS with requested name -
@app.get("/lgs/{lgs_name}")
def read_root(lgs_name: str):

    all_lgs = db["Countries"]
    response = []

    for key, value in all_lgs.items():
        # print (key, value)
        for value in value:
            if lgs_name.upper() in value.upper():
                # print (lgs_name)
                response.append(value)

    return response

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}