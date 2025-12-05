from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from routers import jugadores, partidos
from bd.database import crear_bd_y_tablas

app = FastAPI(title="API Sigmotoa FC")

app.include_router(jugadores.router, prefix="/jugadores", tags=["Jugadores"])
app.include_router(partidos.router, prefix="/partidos", tags=["Partidos"])

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def al_iniciar():
    crear_bd_y_tablas()

@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/docs")