from pydantic import BaseModel


class KindBase(BaseModel):
    id: int
    title: str
