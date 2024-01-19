from fastapi import FastAPI

app = FastAPI()


@app.post("/Patient/")
async def create_patient():
    return {"the created resource"}

@app.get("/Patient/{id}")
async def read_patient(id: int):
    return {f"read resource for {id}"}

@app.put("/Patient/{id}")
async def update_patient(id: int):
    return {"the updated resource for {id}" }

@app.get("/Patient/")
async def search_patient():
    return {"a patient search bundle"}