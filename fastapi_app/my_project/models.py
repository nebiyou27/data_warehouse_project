from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Detection(Base):
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    class_label = Column(String)
    confidence = Column(Float)
    x_center = Column(Float)
    y_center = Column(Float)
    width = Column(Float)
    height = Column(Float)
