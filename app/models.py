from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from .database import Base

## DBに関するあれやこれや。
## カラムの定義や、呼び出すクエリ文を一緒のファイルに書いてるけど本当は分けたほうがいいかも

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)



class ItemBase(BaseModel):
    title: str
    description: str | None = None

from sqlalchemy.orm import Session

def get_item(db: Session, id: int = 0):
    return db.query(models.Item).filter(models.Item.id == id).first()
