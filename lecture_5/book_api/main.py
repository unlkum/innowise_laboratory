from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Book
from schemas import BookCreate, BookOut, BookUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST: create book
@app.post("/books/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


# GET: all books
@app.get("/books/", response_model=list[BookOut])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


# DELETE by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


# PUT: update
@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, update: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    if update.title is not None:
        book.title = update.title
    if update.author is not None:
        book.author = update.author
    if update.year is not None:
        book.year = update.year

    db.commit()
    db.refresh(book)
    return book


# SEARCH
@app.get("/books/search/", response_model=list[BookOut])
def search_books(query: str, db: Session = Depends(get_db)):
    result = (
        db.query(Book)
        .filter((Book.title.ilike(f"%{query}%")) | (Book.author.ilike(f"%{query}%")))
        .all()
    )

    if query.isdigit():
        result_year = db.query(Book).filter(Book.year == int(query)).all()
        result.extend(result_year)

    return result
