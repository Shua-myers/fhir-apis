from collections.abc import Mapping
from typing import Any

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
    # TODO: save to database, handle exceptions
    # TODO: read from database, handle exceptions
    return patient.dict()


@app.get("/Patient/{id}")
async def read_patient(id: int) -> JSONResponse:
    # TODO: read from database with exceptions
    return JSONResponse({"msg": f"read resource for {id}"})


@app.put("/Patient/{id}")
async def update_patient(id: int):
    # TODO: update database, handle exceptions
    return JSONResponse({"msg": f"the updated resource for {id}"})


@app.get("/Patient")
async def search_patient(
    _id: int | None = None, patient: int | None = None, name: str | None = None
):
    # TODO: return all from database
    # TODO: search by id, patient, and name
    # TODO: pagination
    return JSONResponse({"msg": "a patient search bundle"})
