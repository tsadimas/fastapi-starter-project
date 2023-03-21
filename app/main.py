from fastapi import Depends, FastAPI, Security
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from pydantic import Json

from app.db import get_session, init_db
from app.models import Song, SongCreate

from app.deps.auth import get_auth


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
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]


@app.post("/songs")
async def add_song(song: SongCreate, session: AsyncSession = Depends(get_session), identity: Json = Security(get_auth)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song
