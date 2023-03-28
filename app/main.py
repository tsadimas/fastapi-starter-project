from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db import get_session, init_db
from app.models import Song, SongCreate, ArtistCreate, Artist, ArtistwithSongs
from sqlalchemy.orm import selectinload, noload

from app.routes import artist, song

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()



@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


app.include_router(song.router, prefix='/songs',
                   tags=['Songs'])

app.include_router(artist.router, prefix='/artists',
                   tags=['Artists'])
