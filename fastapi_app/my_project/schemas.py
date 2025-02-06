from pydantic import BaseModel

class DetectionSchema(BaseModel):
    image_name: str
    class_label: str
    confidence: float
    x_center: float
    y_center: float
    width: float
    height: float

    class Config:
        orm_mode = True
