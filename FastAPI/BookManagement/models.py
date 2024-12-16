import uuid #universal unique identifier
from typing import Optional
from pydantic import BaseModel, Field

class Book(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    title: str = Field(...)
    author: str = Field(...)
    synopsis: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "...."
            }
        }

class UpdateBook(BaseModel):
    title: Optional[str]
    author: Optional[str]
    synopsis: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Don Quixote",
                "author": "Miguel de Cervantes",
                "synopsis": "Alonso Quixano, a retired country gentleman in his fift"
        }
    }


