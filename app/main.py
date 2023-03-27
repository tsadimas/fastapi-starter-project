from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db import get_session, init_db
from app.models import Song, SongCreate, ArtistCreate, Artist


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()



@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/songs", response_model=list[Song])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return songs


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist_id=song.artist_id)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song


@app.get("/artists", response_model=list[Artist])
async def get_artists(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Artist))
    artists = result.scalars().all()
    return artists

@app.post("/artists")
async def add_artist(artist: ArtistCreate, session: AsyncSession = Depends(get_session)):
    artist = Artist(name=artist.name, surname=artist.surname)
    session.add(artist)
    await session.commit()
    await session.refresh(artist)
    return artist
