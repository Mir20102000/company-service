import pytest
from app.api.models import ClubIn, ClubOut, ClubUpdate

club = ClubIn(
    name='PSG',
    country='France',
    trophies=12
)


def test_create_club(club: ClubIn = club):
    assert dict(club) == {'name': club.name,
                          'country': club.country,
                          'trophies': club.trophies}


def test_update_cast_title(club: ClubIn = club):
    club_upd = ClubOut(
        name='PSG',
        country=club.country,
        trophies=club.trophies,
        id=1
    )
    assert dict(club_upd) == {'name': club.name,
                              'country': club.country,
                              'trophies': club.trophies,
                              'id': club_upd.id
                              }


def test_update_cast_genre(club: ClubIn = club):
    club_upd = ClubOut(
        name=club.name,
        country=club.country,
        trophies=club.trophies,
        id=1
    )
    assert dict(club_upd) == {'name': club.name,
                              'country': club.country,
                              'trophies': club.trophies,
                              'id': club_upd.id}
