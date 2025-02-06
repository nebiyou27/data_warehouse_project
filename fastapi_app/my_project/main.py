from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, crud, schemas

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/detections/", response_model=list[schemas.DetectionSchema])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detections = crud.get_detections(db, skip=skip, limit=limit)
    return detections
