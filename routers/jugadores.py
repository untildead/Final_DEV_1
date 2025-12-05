from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from bd.database import obtener_sesion
from models.models import Jugador

router = APIRouter()

@router.post("/", response_model=Jugador)
def crear_jugador(jugador: Jugador, sesion: Session = Depends(obtener_sesion)):
    sesion.add(jugador)
    sesion.commit()
    sesion.refresh(jugador)
    return jugador

@router.get("/", response_model=list[Jugador])
def leer_jugadores(sesion: Session = Depends(obtener_sesion)):
    jugadores = sesion.exec(select(Jugador)).all()
    return jugadores

@router.get("/{jugador_id}", response_model=Jugador)
def leer_jugador(jugador_id: int, sesion: Session = Depends(obtener_sesion)):
    jugador = sesion.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

@router.put("/{jugador_id}", response_model=Jugador)
def actualizar_jugador(jugador_id: int, jugador_actualizado: Jugador, sesion: Session = Depends(obtener_sesion)):
    jugador = sesion.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    for clave, valor in jugador_actualizado.dict(exclude_unset=True).items():
        setattr(jugador, clave, valor)
    sesion.add(jugador)
    sesion.commit()
    sesion.refresh(jugador)
    return jugador

@router.delete("/{jugador_id}")
def eliminar_jugador(jugador_id: int, sesion: Session = Depends(obtener_sesion)):
    jugador = sesion.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    sesion.delete(jugador)
    sesion.commit()
    return {"mensaje": "Jugador eliminado exitosamente"}