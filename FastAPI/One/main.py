from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#Path Parameters
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Query Parameters
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    print(skip, limit)
    return fake_items_db[skip : skip + limit]

# Type changing query parameters
@app.get("/item/{item_id}")
async def read_item_with_type_change(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item