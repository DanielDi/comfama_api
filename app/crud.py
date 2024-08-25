from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas

def get_afiliados(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Afiliado).offset(skip).limit(limit).all()

def create_afiliado(db: Session, afiliado: schemas.AfiliadoCreate):
    db_afiliado = models.Afiliado(**afiliado.dict())
    db.add(db_afiliado)
    db.commit()
    db.refresh(db_afiliado)
    return db_afiliado
