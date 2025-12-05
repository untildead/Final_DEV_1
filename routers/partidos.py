from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from bd.database import obtener_sesion
from models.models import Partido

router = APIRouter()

@router.post("/", response_model=Partido)
def crear_partido(partido: Partido, sesion: Session = Depends(obtener_sesion)):
    sesion.add(partido)
    sesion.commit()
    sesion.refresh(partido)
    return partido

@router.get("/", response_model=list[Partido])
def leer_partidos(sesion: Session = Depends(obtener_sesion)):
    partidos = sesion.exec(select(Partido)).all()
    return partidos

@router.get("/{partido_id}", response_model=Partido)
def leer_partido(partido_id: int, sesion: Session = Depends(obtener_sesion)):
    partido = sesion.get(Partido, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    return partido

@router.put("/{partido_id}", response_model=Partido)
def actualizar_partido(partido_id: int, partido_actualizado: Partido, sesion: Session = Depends(obtener_sesion)):
    partido = sesion.get(Partido, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    for clave, valor in partido_actualizado.dict(exclude_unset=True).items():
        setattr(partido, clave, valor)
    sesion.add(partido)
    sesion.commit()
    sesion.refresh(partido)
    return partido

@router.delete("/{partido_id}")
def eliminar_partido(partido_id: int, sesion: Session = Depends(obtener_sesion)):
    partido = sesion.get(Partido, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido no encontrado")
    sesion.delete(partido)
    sesion.commit()
    return {"mensaje": "Partido eliminado exitosamente"}