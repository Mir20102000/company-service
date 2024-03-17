from pydantic import BaseModel
from typing import List, Optional


class CompanyIn(BaseModel):
    name: str
    field: str
    year: int


class CompanyOut(CompanyIn):
    id: int


class CompanyUpdate(CompanyIn):
    name: Optional[str] = None
    field: Optional[str] = None
    year: Optional[int] = None
