# FastAPI Sigmotoa FC ₊˚⊹ ᰔ⚽️
## Puedes ver esta aplicación en render ꉂ(˵˃ ᗜ ˂˵)→ https://final-dev-1-6xh4.onrender.com
### API de equipo de futbol -> CRUD para jugadores y partidos -> Analisis de estadisticas
---

## Arquitectura

```
Frontend (HTML) Alojado en render
           ↓
    FastAPI Routers
    ├── /api/jugadores        (CRUD)
    ├── /api/partidos         (CRUD)
           ↓
  SQLite de forma local 
```

---

---

## Requisitos

- Python 3.9+
- pip

**Dependencias principales:** FastAPI, SQLModel, Jinja2

---
**URLs principales:**
- Jugadores: http://localhost:8000/jugadores
- Registros: http://localhost:8000/partidos
- API Docs: http://localhost:8000/docs

---

## API REST - Endpoints Principales

### Jugadores
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/jugadores` | Listar jugadores |
| POST | `/api/jugadores` | Crear jugador |
| GET | `/api/jugadores/{jugador_id}` | Leer jugador |
| PUT | `/api/jugadores/{jugador_id}` | Actualizar jugador |
| DELETE | `/api/jugadores/{jugador_id}` | Eliminar jugador |

### Partidos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/partidos` | Listar partidos |
| POST | `/api/partidos` | Crear partido |
| GET | `/api/partidos/{partido_id}` | Leer partido |
| PUT | `/api/partidos/{partido_id}` | Actualizar |
| DELETE | `/api/partidos/{partido_id}` | Eliminar |


# Instalación y Ejecución Local

## 1. Clonar y preparar el entorno

### Windows PowerShell
```powershell
git clone https://github.com/untildead/Final_DEV_1.git
cd Final_DEV_1
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt


git clone https://github.com/untildead/Final_DEV_1.git
cd Final_DEV_1
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## 2. Ejecutar la aplicación

uvicorn main:app --reload


