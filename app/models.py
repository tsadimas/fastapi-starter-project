from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class ArtistBase(SQLModel):
    name: str
    surname: str

class Artist(ArtistBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    songs: List["Song"] = Relationship(back_populates="artist")

class ArtistCreate(ArtistBase):
    pass
class SongBase(SQLModel):
    name: str
    artist_id: Optional[int] = Field(default=None, foreign_key="artist.id")

class Song(SongBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    artist: Optional[Artist] = Relationship(back_populates="songs")


class SongCreate(SongBase):
    pass


