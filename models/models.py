from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date

class Jugador(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    numero: int
    fecha_nacimiento: str
    nacionalidad: str
    altura: float
    peso: float
    posicion: str
    pie_dominante: str
    estado: str
    estadisticas_acumuladas: str = "0 goles, 0 asistencias"

    partidos: List["Partido"] = Relationship(back_populates="jugador")

class Partido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: date
    rival: str
    condicion: str
    goles: int
    tarjetas: int
    faltas: int
    minutos_jugados: int
    resultado: str

    jugador_id: int = Field(foreign_key="jugador.id")
    jugador: Jugador = Relationship(back_populates="partidos")