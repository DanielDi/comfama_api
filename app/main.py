from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import app.schemas as schemas
import app.crud as crud
import app.models as models
from app.database import SessionLocal, engine
from app.security import get_current_active_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Obtener sesión para la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/afiliados", response_model=List[schemas.Afiliado])
async def read_afiliados(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    afiliados = crud.get_afiliados(db, skip=skip, limit=limit)
    return afiliados

@app.post("/afiliados", response_model=schemas.Afiliado)
async def create_afiliado(afiliado: schemas.AfiliadoCreate, db: Session = Depends(get_db)):
    return crud.create_afiliado(db=db, afiliado=afiliado)
