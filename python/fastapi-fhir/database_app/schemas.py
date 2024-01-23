# Doing this for learning sake (https://fastapi.tiangolo.com/tutorial/sql-databases/) and to share as an example
# A future iteration will explore using fhir.resources which already include Pydantic FHIR schemas/models

from uuid import uuid4, UUID
from datetime import datetime
from pydantic import BaseModel, Field, PositiveInt


class Name(BaseModel):
    id: int
    uuid: UUID = Field(default_factory=uuid4)
    use: str
    text: str
    family: str
    given: list[str] = []
    prefix: list[str] = []
    suffix: list[str] = []
    begin_effective_dt_tm: datetime = Field(default_factory=datetime.now)
    end_effective_dt_tm: datetime  # TODO: add default for 12-31-2100

    class Config:
        orm_mode = True


class Telecom(BaseModel):
    id: int
    uuid: UUID = Field(default_factory=uuid4)
    system: str
    value: str
    use: str
    rank: PositiveInt
    begin_effective_dt_tm: datetime = Field(default_factory=datetime.now)
    end_effective_dt_tm: datetime  # TODO: add default for 12-31-2100

    class Config:
        orm_mode = True


class Patient(BaseModel):
    id: int
    uuid: UUID = Field(default_factory=uuid4)
    active: bool = True
    names: list[Name] = []
    telecoms: list[Telecom] = []
    gender: str
    birthDate: datetime

    class Config:
        orm_mode = True
