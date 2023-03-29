from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db import get_session
from app.models import ArtistCreate, Artist, ArtistwithSongs
from sqlalchemy.orm import selectinload, noload

router = APIRouter()


@router.get("/", response_model=list[ArtistwithSongs])
async def get_artists(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Artist).options(selectinload(Artist.songs)))
    artists = result.scalars().all()
    return artists


@router.post("/")
async def add_artist(artist: ArtistCreate, session: AsyncSession = Depends(get_session)):
    artist = Artist(name=artist.name, surname=artist.surname)
    session.add(artist)
    await session.commit()
    await session.refresh(artist)
    return artist
