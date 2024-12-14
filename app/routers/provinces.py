from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.province import Province
from schemas.province import ProvinceResponse
from database.database import SessionLocal
router = APIRouter()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/provinces/", response_model=list[ProvinceResponse])
def get_all_provinces(db: Session = Depends(get_db)):
    provinces = db.query(Province).all()
    return provinces