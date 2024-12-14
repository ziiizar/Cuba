# import uvicorn
from database.database import Base,engine
from fastapi import FastAPI
from database.database import SessionLocal
from models.province import Province
from models.town import Town
from routers.provinces import router as province_router
from routers.towns import router as town_router

app = FastAPI()

Base.metadata.create_all(bind=engine)




@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(province_router, prefix="/api")
app.include_router(town_router, prefix="/api")


