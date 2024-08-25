from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from uuid import uuid4
from app.database import Base

class Afiliado(Base):
    __tablename__ = "afiliados"

    id = Column(pgUUID(as_uuid=True), primary_key=True, default=uuid4)
    nombres = Column(String, index=True)
    apellidos = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    estado = Column(String)
