from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str
    description: str

class CategoryRequest(BaseModel):
    name: str
    description: str

class CategoryResponse(CategoryRequest):
    id: int