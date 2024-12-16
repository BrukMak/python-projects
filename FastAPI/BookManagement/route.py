from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from  models import Book, UpdateBook

router = APIRouter()

@router.post("/", response_description="Add new book", status_code=status.HTTP_201_CREATED, response_model=Book)
def create_book(request: Request, book: Book = Body(...)):
    book = jsonable_encoder(book)
    new_book = request.app.database["books"].insert_one(book)
    created_book = request.app.database["books"].find_one({"_id": new_book.inserted_id})

    return created_book

@router.get("/", response_description="List all books", response_model=List[Book])
def list_books(request: Request):
    books = list(request.app.database["books"].find(limit=100))
    return books

@router.get("/{id}", response_description="Get a single book", response_model=Book)
def show_book(request: Request, id: str):
    if (book := request.app.database["books"].find_one({"_id": id})) is not None:
        return book

    raise HTTPException(status_code=404, detail=f"Book with id {id} not found")

@router.put("/{id}", response_description="Update a book", response_model=Book)
def update_book(request: Request, id: str, book: UpdateBook = Body(...)):
    book = {k: v for k, v in book.dict().items() if v is not None}

    if len(book) >= 1:
        updated_book = request.app.database["books"].find_one_and_update({"_id": id}, {"$set": book}, return_document=True)
        return updated_book

    raise HTTPException(status_code=404, detail=f"Book with id {id} not found")

@router.delete("/{id}", response_description="Delete book")
def delete_book(request: Request, id: str):
    delete_book = request.app.database["books"].delete_one({"_id": id})

    if delete_book.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Book with id {id} not found")