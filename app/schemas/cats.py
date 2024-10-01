from pydantic import BaseModel


class CreateCatSchema(BaseModel):
    kind: str
    age: int
    color: str
    description: str


class CatSchema(BaseModel):
    id: int
    kind: int
    age: int
    color: str
    description: str
