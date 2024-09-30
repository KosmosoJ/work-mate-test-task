from pydantic import BaseModel


class CreateCatSchema(BaseModel):
    kind:str
    age:int
    description:str 
    
class CatSchema(BaseModel):
    id:int
    kind:int
    age:int
    description:str
    
