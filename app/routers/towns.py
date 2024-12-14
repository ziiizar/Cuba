from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.town import Town
from schemas.town import TownResponse
from database.database  import SessionLocal
router = APIRouter()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/towns/", response_model=list[TownResponse])
def get_all_towns(db: Session = Depends(get_db)):
    towns = db.query(Town).all()
    return towns