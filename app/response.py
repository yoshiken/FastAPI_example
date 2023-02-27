from http.client import HTTPException

## 来た値によって実際に返すやーつ
## handlerは最終的にここの関数を呼ぶ
## ここでは一切の加工を行わない

def read_root():
    return {"Hello": "World"}

def read_item(result):
    return {"item_id": result.id, "title": result.title, "description": result.description}

def none_item(e):
    return HTTPException(status_code=404, detail=e)
