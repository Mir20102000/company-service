from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import CompanyOut, CompanyIn, CompanyUpdate
from app.api import db_manager

companies = APIRouter()

@companies.post('/', response_model=CompanyOut, status_code=201) #localhost:8002/api/v1/casts
async def create_company(payload: CompanyIn):
    company_id = await db_manager.add_company(payload)

    response = {
        'id': company_id,
        **payload.dict()
    }

    return response


@companies.get('/', response_model=List[CompanyOut]) #localhost:8001/api/v1/animes
async def get_companies():
    return await db_manager.get_all_company()
