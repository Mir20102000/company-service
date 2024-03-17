import pytest
from app.api.models import CompanyIn, CompanyOut, CompanyUpdate

company = CompanyIn(
    name='Samsung',
    field='Technology',
    year=1969
)


def test_create_company(company: CompanyIn = company):
    assert dict(company) == {'name': company.name,
                          'field': company.field,
                          'year': company.year}


def test_update_cast_title(company: CompanyIn = company):
    company_upd = CompanyOut(
        name='Samsung',
        field=company.field,
        year=company.year,
        id=1
    )
    assert dict(company_upd) == {'name': company.name,
                              'field': company.field,
                              'year': company.year,
                              'id': company_upd.id
                              }


def test_update_cast_genre(company: CompanyIn = company):
    company_upd = CompanyOut(
        name=company.name,
        field=company.field,
        year=company.year,
        id=1
    )
    assert dict(company_upd) == {'name': company.name,
                              'field': company.field,
                              'year': company.year,
                              'id': company_upd.id}
