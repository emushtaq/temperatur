from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.converter import Converter

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_items_db = [{"C_F": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/convert")
async def read_item(
        source: str,
        destination: str,
        value: str):
    if not value.isnumeric():
        raise HTTPException(status_code=400, detail='Invalid value passed. Value must be a valid Integer or Float only')

    if not isinstance(source, str) or source not in ['C', 'K', 'F']:
        raise HTTPException(status_code=400, detail='Invalid source passed. Value must be one of "C", "K" or "F"')

    if not isinstance(destination, str) or destination not in ['C', 'K', 'F']:
        raise HTTPException(status_code=400, detail='Invalid destination passed. Value must be one of "C", "K" or "F"')

    return Converter(source, destination).convert(float(value))
