from fastapi import FastAPI

app = FastAPI()


@app.get("/Patient/{id}")
async def read_patient(id: int):
    return {"patient": id}