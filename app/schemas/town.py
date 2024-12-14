from pydantic import BaseModel

class TownBase(BaseModel):
    name: str
    province_id: int


class TownResponse(TownBase):
    id: int
    name: str

    class Config:
        orm_mode = True
