from app.api.models import CompanyIn, CompanyOut, CompanyUpdate
from app.api.db import companies, database


async def add_company(payload: CompanyIn):
    query = companies.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_company():
    query = companies.select()
    return await database.fetch_all(query=query)
