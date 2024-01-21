from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# fhir.resources could do this for us
class Patient(BaseModel):
    id: str
    active: bool = True
    name: dict
    telecom: dict | None = None
    gender: str
    birthDate: str


app = FastAPI()


@app.post("/Patient/")
async def create_patient(patient: Patient):
    # TODO: save to database
    return patient


@app.get("/Patient/{id}")
async def read_patient(id: int):
    return {f"read resource for {id}"}


@app.put("/Patient/{id}")
async def update_patient(id: int):
    return {"the updated resource for {id}"}


@app.get("/Patient/")
async def search_patient(
    _id: int | None = None, patient: int | None = None, name: str | None = None
):
    return {"a patient search bundle"}
