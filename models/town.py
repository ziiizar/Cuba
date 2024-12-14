from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
# Modelo para los municipios
class Town(Base):
    __tablename__ = "towns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    province_id = Column(Integer, ForeignKey("provinces.id"), nullable=False)

    # Relación con la provincia
    province = relationship("Province", back_populates="towns")
