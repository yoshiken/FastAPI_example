from .database import SessionLocal, engine
from . import models

## 俗に言うビジネスロジック
## 必要であればDB呼んだり、加工したり諸々
## エラー時はraiseで例外を投げる。

class NoneException(Exception):
    pass

def read_item(item_id: int, q: str = ""):
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    item = models.get_item(db, item_id)
    if item is None:
        raise NoneException("item_id is not found")
    ## itemを元にさらなる呼び出しや加工したり(めんどくて書いてない
    return {"item_id": item_id, "q": q}
