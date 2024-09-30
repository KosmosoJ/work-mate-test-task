from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base 


class Kind(Base):
    __tablename__ = 'kinds'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(), nullable=False)
    
class Cat(Base):
    __tablename__ = 'cats'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    kind = Column(ForeignKey('kinds.id', ondelete='SET NULL'), nullable=False)
    age = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
