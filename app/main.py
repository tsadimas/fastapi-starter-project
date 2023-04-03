from fastapi import Depends, FastAPI, Security
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from pydantic import Json

from app.db import get_session, init_db
from app.models import Song, SongCreate, ArtistCreate, Artist, ArtistwithSongs
from sqlalchemy.orm import selectinload, noload
from fastapi.middleware.cors import CORSMiddleware

from app.deps.auth import get_auth

from app.routes import artist, song

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://frontend:8080",
    "http://localhost:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
