from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db import get_session
from app.models import Song, SongCreate
from sqlalchemy.orm import selectinload, noload

router = APIRouter()


@router.get("/", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return songs


@router.post("/")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist_id=song.artist_id)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
