from . import response
form . import service

## hanlderは"呼び出す関数を変えるだけ"の役割
## handler自体で変数の加工や作成は基本しない

def read_root():
    return response.read_root()

def read_item(item_id: int, q: str = ""):
    try:
        with service.read_item(item_id, q) as result:
            return response.read_item(result)
    except service.NoneException as e:
        return response.none_item(e)
