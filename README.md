Instalación y Ejecución Local
    1. Clonar y preparar entorno
    # Windows PowerShell
    git clone https://github.com/untildead/Final_DEV_1.git
    cd sleephabits-main
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

    # Linux/Mac
    source .venv/bin/activate
    pip install -r requirements.txt

2. Ejecutar la aplicación

    uvicorn main:app --reload

