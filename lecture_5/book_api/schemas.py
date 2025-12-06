from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    year: int | None = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None


class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True
