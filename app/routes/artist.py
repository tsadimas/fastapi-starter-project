from fastapi import Depends, FastAPI, APIRouter,  Security
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from pydantic import Json

from app.db import get_session
from app.models import ArtistCreate, Artist, ArtistwithSongs
from sqlalchemy.orm import selectinload, noload
from app.deps.auth import get_auth

router = APIRouter()


@router.get("/", response_model=list[ArtistwithSongs])
async def get_artists(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Artist).options(selectinload(Artist.songs)))
    artists = result.scalars().all()
    return artists


@router.post("/")
async def add_artist(artist: ArtistCreate, session: AsyncSession = Depends(get_session), identity: Json = Security(get_auth)):
    artist = Artist(name=artist.name, surname=artist.surname)
    session.add(artist)
    await session.commit()
    await session.refresh(artist)
    return artist
