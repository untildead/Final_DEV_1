# FastAPI Sigmotoa FC
## Puedes ver esta aplicación en render https://final-dev-1-6xh4.onrender.com
### API de equipo de futbol -> CRUD para jugadores y partidos -> Analisis de estadisticas
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
