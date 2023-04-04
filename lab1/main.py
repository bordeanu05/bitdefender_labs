from typing import Union
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()

class PostClass(BaseModel):
    a: int
    b: int
    
@app.post("/postoperations")
def post(post: PostClass):
    return {"suma": post.a + post.b}

@app.get("/operations/{a}?{b}")
def get_operations(a: int, b: int, c: int = 1):
    return {"suma": a + b,
            "diferenta:" : a-b,
            "produs:" : a*b,
            "impartire:" : a/b,}

@app.get("/")
def read_root():
    return {"Bit": "Defender"}


@app.get("/items/{aaa}")
def read_item(aaa: int, q: Union[str, None] = None):
    return {"item_id": aaa, "q": q}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)