# Doing this for learning sake (https://fastapi.tiangolo.com/tutorial/sql-databases/) and to share as an example
# A future iteration will explore using fhir.resources or scraping from https://hl7.org/ to model the data.
import enum

from sqlalchemy import (
    ARRAY,
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Uuid,
)
from sqlalchemy.orm import relationship

from .database import Base


class NameUseEnum(enum.Enum):
    usual = 1
    official = 2
    temp = 3
    nickname = 4
    anonymous = 5
    old = 6
    maiden = 7


class TelecomUseEnum(enum.Enum):
    home = 1
    work = 2
    temp = 3
    old = 4
    mobile = 5


class SystemEnum(enum.Enum):
    phone = 1
    fax = 2
    email = 3
    pager = 4
    url = 5
    sms = 6
    other = 7


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    uuid = Column(Uuid)
    active = Column(Boolean, default=True)
    gender = Column(String)
    birthDate = Column(String)

    names = relationship("Name", back_populates="patients")
    telecoms = relationship("Telecom", back_populates="patients")


class Name(Base):
    __tablename__ = "names"

    id = Column(Integer, primary_key=True)
    uuid = Column(Uuid)
    use = Column(Enum(NameUseEnum, validate_strings=True))
    text = Column(String)
    family = Column(String)
    given = Column(ARRAY(String))
    prefix = Column(ARRAY(String))
    suffix = Column(ARRAY(String))
    begin_effective_dt_tm = Column(DateTime)
    end_effective_dt_tm = Column(DateTime)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    patient = relationship("Patient", back_populates="names")


class Telecom(Base):
    __tablename__ = "telecoms"

    id = Column(Integer, primary_key=True)
    uuid = Column(Uuid)
    system = Column(Enum(SystemEnum, validate_strings=True))
    value = Column(String)
    use = Column(Enum(TelecomUseEnum, validate_strings=True))
    rank = Column(SmallInteger, CheckConstraint("rank>0"))
    begin_effective_dt_tm = Column(DateTime)
    end_effective_dt_tm = Column(DateTime)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    patient = relationship("Patient", back_populates="telecoms")
