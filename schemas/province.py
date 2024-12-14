from pydantic import BaseModel
from schemas.town import TownResponse

class ProvinceBase(BaseModel):
    name: str


class ProvinceResponse(ProvinceBase):
    id: int
    name: str
    towns: list[TownResponse] = []

    class Config:
        orm_mode = True
