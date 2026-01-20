from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Priority(str, Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"

class Task(BaseModel):
    id: int
    titulo: str = Field(..., min_length=3, max_length=50)
    descricao: Optional[str] = None
    prioridade: Priority = Priority.MEDIA
    concluida: bool = False