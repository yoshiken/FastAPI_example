from fastapi import FastAPI
from . import handler


## 来たリクエストによって呼ぶhanderを変えるだけ。
## responseもhandlerが制御するからそのままreturn

app = FastAPI()

@app.get("/")
def read_root():
    return handler.read_root()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = ""):
    return handler.read_item(item_id, q)
