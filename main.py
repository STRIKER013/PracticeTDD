from typing import Union

from fastapi import FastAPI

#from FuncionesPY import hellowFastApiPY

app = FastAPI()


@app.get("/")
def helloFastApiPy():
    return {"Hello FastApi"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}