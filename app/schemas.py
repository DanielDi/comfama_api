from pydantic import BaseModel, EmailStr
from uuid import UUID

class AfiliadoBase(BaseModel):
    nombres: str
    apellidos: str
    email: EmailStr
    estado: str

class AfiliadoCreate(AfiliadoBase):
    pass

class Afiliado(AfiliadoBase):
    id: UUID

    class Config:
        orm_mode = True
